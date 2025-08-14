from django.db import models
from .utility import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator



class Profile(BaseModel):
    name = models.CharField(max_length=100, verbose_name='نام')
    title = models.CharField(max_length=200, verbose_name='عنوان شغلی')
    bio = models.TextField(verbose_name='بیوگرافی')
    profile_image = models.ImageField(
        upload_to='profile/', 
        null=True, 
        blank=True,
        verbose_name='تصویر پروفایل'
    )
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, blank=True, verbose_name='تلفن')
    location = models.CharField(max_length=100, blank=True, verbose_name='محل زندگی')
    resume = models.FileField(
        upload_to='resume/', 
        null=True, 
        blank=True,
        verbose_name='فایل رزومه'
    )

    social_links = models.JSONField(default=dict, blank=True, null=True)






class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مهارت')
    
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='درصد تسلط'
    )

    description = models.TextField(blank=True, verbose_name='توضیحات')
    
    is_featured = models.BooleanField(default=False, verbose_name='مهارت برجسته')

    icon_class = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='کلاس آیکن (FontAwesome)',
        help_text='مثلاً: fab fa-python'
    )

    icon_image = models.ImageField(
        upload_to='skill_icons/',
        blank=True,
        null=True,
        verbose_name='آیکن تصویری'
    )

    def __str__(self):
        return self.name


class Technology(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='نام تکنولوژی')
    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='آیکون',
        help_text='کلاس FontAwesome مثل: fab fa-python'
    )

    color = models.CharField(
        max_length=7,
        blank=True,
        verbose_name='رنگ',
        help_text='مثلاً: #3776AB'
    )

    icon_image = models.ImageField(
        upload_to='tech_icons/',
        blank=True,
        null=True,
        verbose_name='آیکون تصویری'
    )

    class Meta:
        verbose_name = 'تکنولوژی'
        verbose_name_plural = 'تکنولوژی‌ها'

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته‌بندی')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'دسته‌بندی پروژه'
        verbose_name_plural = 'دسته‌بندی‌های پروژه'

    def __str__(self):
        return self.name
    



class Project(BaseModel):

    STATUS_CHOICES = [
        ('completed', 'تکمیل شده'),
        ('in_progress', 'در حال انجام'),
        ('on_hold', 'متوقف شده'),
    ]

    title = models.CharField(max_length=200, verbose_name='عنوان پروژه')
    description = models.TextField(verbose_name='توضیحات')
    short_description = models.CharField(
        max_length=300, 
        verbose_name='توضیح کوتاه'
    )
    category = models.ForeignKey(
        ProjectCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='projects'
    )
    technologies = models.ManyToManyField(
        Technology, 
        related_name='projects',
        verbose_name='تکنولوژی‌ها'
    )
    featured_image = models.ImageField(
        upload_to='projects/', 
        verbose_name='تصویر اصلی'
    )
    github_url = models.URLField(blank=True, verbose_name='لینک گیت‌هاب')
    demo_url = models.URLField(blank=True, verbose_name='لینک دمو')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='completed'
    )

    is_featured = models.BooleanField(default=False, verbose_name='پروژه برجسته')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'
        ordering = ['-is_featured', 'order', '-created_at']

    def __str__(self):
        return self.title
    


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, verbose_name='عنوان')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب')

    class Meta:
        ordering = ['order']
        verbose_name = 'تصویر پروژه'
        verbose_name_plural = 'تصاویر پروژه'

