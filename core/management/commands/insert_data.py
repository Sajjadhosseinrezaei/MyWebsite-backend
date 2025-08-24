import io
import uuid
import random
import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from faker import Faker
from core.models import Skill, Technology, ProjectCategory, Project, ProjectImage


class Command(BaseCommand):
    help = "Populate the database with test data (with random web images) while avoiding duplicates."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    # ---------- تنظیمات تصاویر ----------
    # برای کاهش حجم و سرعت بیشتر می‌تونید ابعاد رو کوچیک‌تر کنید.
    FEATURED_W, FEATURED_H = 1200, 800
    GALLERY_W, GALLERY_H = 1000, 700

    # می‌تونید کلمات کلیدی بسازید و از سرویس‌های موضوع‌محور استفاده کنید.
    # در صورت نیاز، آدرس Unsplash رو جایگزین کنید (ممکنه rate-limit داشته باشه).
    def random_image_url(self, width=800, height=600):
        # Picsum: تصویر تصادفی با cache-buster
        return f"https://picsum.photos/{width}/{height}?random={random.randint(1, 10_000_000)}"

    def fetch_image_bytes(self, url: str) -> bytes:
        """
        تصویر را دانلود می‌کند و بایت‌های آن را برمی‌گرداند.
        در صورت خطا، استثنا raise می‌شود.
        """
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        return resp.content

    def save_imagefield_from_url(self, instance, field_name: str, url: str, ext: str = "jpg"):
        """
        یک URL تصویر دریافت می‌کند، دانلود می‌کند و در فیلد ImageField ذخیره می‌کند.
        """
        raw = self.fetch_image_bytes(url)
        filename = f"{uuid.uuid4().hex}.{ext}"
        content = ContentFile(raw)
        getattr(instance, field_name).save(filename, content, save=False)

    def handle(self, *args, **options):
        # --------- لیست نام‌های ثابت برای جلوگیری از تکرار ----------
        skill_names = ['Python', 'Django', 'JavaScript', 'React', 'SQL']
        tech_names = ['NodeJS', 'VueJS', 'Docker', 'PostgreSQL', 'MongoDB', 'Redis', 'AWS', 'Git', 'HTML', 'CSS']
        category_names = ['Web Development', 'Mobile Apps', 'Data Science']

        # --------- ایجاد مهارت‌ها (Skills) بدون تکرار ----------
        skills = []
        for name in skill_names:
            skill, _ = Skill.objects.get_or_create(
                name=name,
                defaults={
                    'level': random.randint(50, 100),
                    'description': self.fake.paragraph(),
                    'is_featured': random.choice([True, False]),
                    'icon_class': f'fab fa-{self.fake.word()}',
                }
            )
            skills.append(skill)

        # --------- ایجاد تکنولوژی‌ها (Technologies) بدون تکرار ----------
        technologies = []
        for name in tech_names:
            tech, _ = Technology.objects.get_or_create(
                name=name,
                defaults={
                    'icon': f'fab fa-{self.fake.word()}',
                    'color': self.fake.hex_color(),
                }
            )
            technologies.append(tech)

        # --------- ایجاد دسته‌بندی‌های پروژه (ProjectCategories) بدون تکرار ----------
        categories = []
        for name in category_names:
            category, _ = ProjectCategory.objects.get_or_create(
                name=name,
                defaults={
                    'description': self.fake.paragraph(),
                    'slug': self.fake.slug()
                }
            )
            categories.append(category)

        # --------- ایجاد پروژه‌ها (Projects) + تصاویر وب ----------
        # تعداد پروژه‌ها را در صورت نیاز تغییر دهید
        num_projects = 20

        created_projects = 0
        for i in range(num_projects):
            title = f"{self.fake.sentence(nb_words=3).strip('.')} {i+1}"
            project, created = Project.objects.get_or_create(
                title=title,
                defaults={
                    'description': self.fake.paragraph(),
                    'short_description': self.fake.sentence(nb_words=10),
                    'category': random.choice(categories) if categories else None,
                    # توجه: اگر فیلد featured_image از نوع ImageField است، در ادامه با save() مقداردهی می‌شود
                    'github_url': self.fake.url(),
                    'demo_url': self.fake.url(),
                    'status': random.choice(['completed', 'in_progress', 'on_hold']),
                    'is_featured': random.choice([True, False]),
                    'order': random.randint(0, 100)
                }
            )

            # ست کردن تکنولوژی‌های تصادفی
            project.technologies.set(
                random.sample(technologies, k=random.randint(1, min(5, len(technologies))))
            )

            # اگر پروژه تازه ساخته شده یا تصویر شاخص ندارد، تصویر وب را دانلود و ذخیره کن
            if created or not getattr(project, 'featured_image', None):
                try:
                    url = self.random_image_url(self.FEATURED_W, self.FEATURED_H)
                    self.save_imagefield_from_url(project, 'featured_image', url)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"[Project Featured Image] Failed: {e}"))

            # ذخیره‌ی پروژه بعد از اعمال تغییرات فیلدهای فایل
            project.save()
            if created:
                created_projects += 1

            # ایجاد 1 تا 3 تصویر گالری برای هر پروژه
            num_images = random.randint(1, 3)
            for j in range(num_images):
                caption = f"{self.fake.sentence(nb_words=5)} {j+1}"
                # برای جلوگیری از تکرار تصویر با کپشن یکسان، get_or_create بر اساس (project, caption)
                pimg, pimg_created = ProjectImage.objects.get_or_create(
                    project=project,
                    caption=caption,
                    defaults={'order': random.randint(0, 100)}
                )
                # اگر تازه ساخته شده یا تصویر ندارد، تصویر وب را دانلود و ذخیره کن
                if pimg_created or not getattr(pimg, 'image', None):
                    try:
                        url = self.random_image_url(self.GALLERY_W, self.GALLERY_H)
                        self.save_imagefield_from_url(pimg, 'image', url)
                        pimg.save()
                    except Exception as e:
                        self.stdout.write(self.style.WARNING(f"[ProjectImage] Failed: {e}"))

        self.stdout.write(self.style.SUCCESS(
            f"Seeding done. Projects created: {created_projects} / {num_projects}"
        ))
