# MyWebsite-backend

> Full-featured backend for a personal portfolio website — Django + DRF

---

## 🇮🇷 فارسی — ویژگی‌ها

* پنل ادمین **کاملاً فارسی‌سازی‌شده**
* گالری پروژه با آپلود نامحدود تصاویر و مرتب‌سازی کشیدن و رها کردن
* سطح مهارت **0–100%** همراه با آیکن FontAwesome یا تصویر دلخواه
* وضعیت پروژه: **تکمیل‌شده / در حال انجام / متوقف**
* پرچم **برجسته** برای مهارت‌ها و پروژه‌ها
* ذخیرهٔ لینک‌های اجتماعی به‌صورت **JSON انعطاف‌پذیر**
* مستندات API خودکار با **Swagger & ReDoc**
* Endpoint چک سلامت برای مانیتورینگ
* آماده برای **PostgreSQL** و اجرا در **Docker**

---

## 🌟 English — Features

* Fully localized Persian admin
* Unlimited project gallery with drag-and-drop ordering
* Skill levels 0–100% with FontAwesome or custom icons
* Project status: completed / in-progress / on-hold
* Featured flag for skills & projects
* Social links stored as flexible JSON
* Auto-generated API docs (Swagger & ReDoc)
* Health-check endpoint for uptime monitoring
* Ready for PostgreSQL & Docker

---

## 🧰 تکنولوژی‌ها / Tech Stack

| لایه / Layer         | فناوری / Tech                      |
| -------------------- | ---------------------------------- |
| بک‌اند / Backend     | Django 4.2 LTS                     |
| API                  | Django REST Framework 3.14         |
| مستندات / Docs       | drf-spectacular (OpenAPI 3)        |
| ذخیره‌سازی / Storage | Pillow / AWS S3 / Cloudinary       |
| پایگاه‌داده / DB     | PostgreSQL (local: SQLite for dev) |
| دیپلوی / Deploy      | Gunicorn + Nginx + Docker          |

---

## ⚙️ راه‌اندازی سریع / Quick start

```bash
git clone https://github.com/Sajjadhosseinrezaei/MyWebsite-backend.git
cd MyWebsite-backend

# ساخت محیط مجازی
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt

# متغیرهای محیطی را از .env.example کپی کنید و تنظیمات لازم را انجام دهید
cp .env.example .env
# سپس مهاجرت‌ها و ادمین را بسازید
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# مستندات Swagger در:
# http://localhost:8000/api/schema/swagger-ui/
```

---

## 🔐 متغیرهای محیطی (.env)

نمونه‌ها — **مقادیر واقعی را وارد کنید**:

```
SECRET_KEY=your-secret-key
DEBUG=0
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=postgres://user:pass@host:5432/dbname
LIARA_ACCESS_KEY=xxx
LIARA_SECRET_KEY=yyy
BUCKET_NAME=mybucket
LIARA_ENDPOINT_URL=https://storage.iran.liara.space
MAIL_HOST=smtp.example.com
MAIL_PORT=465
MAIL_USER=you@example.com
MAIL_PASSWORD=strongpass
MAIL_FROM_ADDRESS=you@example.com
TURNSTILE_SECRET_KEY=your-turnstile-secret
```

نکته‌ها:

* `DEBUG=False` را در محیط تولید تنظیم کنید.
* از یک **SECRET_KEY** قوی و منحصر‌به‌فرد استفاده کنید.
* `DATABASE_URL` برای اتصال به PostgreSQL استفاده می‌شود؛ برای توسعه محلی می‌توانید SQLite داشته باشید.

---

## 📡 API Endpoints (خلاصه)

| متد / Method | مسیر / Endpoint            | توضیح / Description     |
| -----------: | -------------------------- | ----------------------- |
|          GET | `/api/profile/`            | اطلاعات عمومی پروفایل   |
|          GET | `/api/skills/`             | فهرست مهارت‌ها          |
|          GET | `/api/technologies/`       | فهرست تکنولوژی‌ها       |
|          GET | `/api/project-categories/` | دسته‌بندی پروژه‌ها      |
|          GET | `/api/projects/`           | همهٔ پروژه‌ها           |
|          GET | `/api/projects/featured/`  | پروژه‌های برجسته        |
|         POST | `/api/contact/`            | ارسال پیام تماس         |
|          GET | `/api/health/`             | وضعیت سلامت سرور        |
|          GET | `/api/schema/swagger-ui/`  | Swagger UI (تعامل‌پذیر) |
|          GET | `/api/schema/redoc/`       | ReDoc docs              |

---

## 🐳 Docker (Production)

فایل‌های `docker-compose.yml` و کانفیگ Nginx برای راه‌اندازی production آماده‌اند.

```bash
# در دایرکتوری پروژه
docker-compose up -d --build
```

کانتینرها معمولاً شامل: PostgreSQL، وب (Django+Gunicorn)، و Nginx برای سرو استاتیک و روتینگ هستند.

---

## 📸 اسکرین‌شات‌ها

* `docs/skills.png` — پنل ادمین مهارت‌ها
* `docs/projects.png` — پنل ادمین پروژه‌ها

(اگر تصاویر در مسیر دیگری هستند یا نیاز به به‌روزرسانی دارند، مسیرها را اصلاح کنید.)

---

## 🧪 تست

```bash
python manage.py test
```

نکته: قبل از اجرای تست‌ها از تنظیمات دیتابیس تست مناسب استفاده کنید یا `DATABASE_URL` مخصوص تست تعریف کنید.

---

## 🚢 چک‌لیست دیپلوی / Deployment checklist

* `DEBUG=False` و `SECRET_KEY` قوی
* `collectstatic` اجرا شده
* `ALLOWED_HOSTS` تنظیم شده
* از PostgreSQL در production استفاده کنید
* فایل‌های استاتیک/مدیا توسط Nginx یا سرویس Cloud (S3, Cloudflare R2, Liara Storage) سرو شوند
* HTTPS فعال (Let’s Encrypt یا CA دیگر)
* CI/CD: GitHub Actions یا هر ابزار منتخب برای استقرار خودکار
* مانیتورینگ و alert برای endpoint `GET /api/health/`

---

## 🤝 مشارکت / Contributing

1. Fork کنید
2. شاخهٔ جدید بسازید:

   ```bash
   ```

git checkout -b feature/awesome

````
3. تغییرات را commit کنید:
```bash
git commit -m "Add awesome feature"
````

4. Push و Pull Request بزنید

لطفاً قبل از PR توضیحات مربوط به تغییرات، تست‌ها و نکات مهاجرت را اضافه کنید.

---

## 📄 مجوز / License

MIT © Sajjad Rezaei

---

## 📬 ارتباط / Contact

* Email: [sajjadhosseinrezaei@yahoo.com](mailto:sajjadhosseinrezaei@yahoo.com)
* LinkedIn: [https://linkedin.com/in/sajjadhosseinrezaei](https://linkedin.com/in/sajjadhosseinrezaei)
* Website: [https://sajjadhosseinrezaei.ir](https://sajjadhossein.site)

---

Made with ❤️ in Django
