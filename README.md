🇮🇷 فارسی | Persian
🌟 ویژگی‌ها
پنل ادمین کاملاً فارسی
آپلود بی‌نهایت تصویر برای هر پروژه
سطح مهارت ۰–۱۰۰٪ + آیکن FontAwesome یا تصویر دلخواه
وضعیت پروژه: تکمیل‌شده / در حال انجام / متوقف
پرچم «برجسته» برای مهارت‌ها و پروژه‌ها
لینک‌های اجتماعی دلخواه (JSON)
Swagger & ReDoc برای مستندات API
Health-check برای مانیتورینگ

آماده برای PostgreSQL و Docker

🧰 تکنولوژی‌ها


| لایه        | فناوری                       |
| ----------- | ---------------------------- |
| بک‌اند      | Django 4.2 LTS               |
| API         | Django REST Framework 3.14   |
| مستندات     | drf-spectacular (OpenAPI 3)  |
| ذخیره‌سازی  | Pillow / AWS-S3 / Cloudinary |
| پایگاه‌داده | PostgreSQL (محلی: SQLite)    |
| دیپلوی      | Gunicorn + Nginx + Docker    |


⚙️ نصب و راه‌اندازی سریع

git clone https://github.com/Sajjadhosseinrezaei/MyWebsite-backend.git
cd MyWebsite-backend

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # تنظیمات دیتابیس و ایمیل را کامل کنید
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
حالا به http://localhost:8000/api/schema/swagger-ui/ بروید.
🔐 متغیرهای محیطی (.env)

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
📡 اندپوینت‌های API
Table
متد	مسیر	توضیح
GET	/api/profile/	اطلاعات پروفایل
GET	/api/skills/	فهرست مهارت‌ها
GET	/api/technologies/	تکنولوژی‌ها
GET	/api/project-categories/	دسته‌بندی پروژه‌ها
GET	/api/projects/	همه‌ی پروژه‌ها
GET	/api/projects/featured/	پروژه‌های برجسته
POST	/api/contact/	ارسال پیام تماس
GET	/api/health/	چک سلامت سرور
GET	/api/schema/swagger-ui/	مستندات تعاملی Swagger
GET	/api/schema/redoc/	مستندات ReDoc
🐳 Docker (پروداکشن)
bash
docker-compose up -d
شامل: PostgreSQL، وب (Django+Gunicorn)، Nginx
📸 اسکرین‌شات‌ها
Table

ادمین مهارت‌ها	ادمین پروژه‌ها
docs/skills.png	docs/projects.png
🧪 تست
bash

python manage.py test
🚢 چک‌لیست دیپلوی
DEBUG=False و SECRET_KEY قوی
collectstatic اجرا شود
ALLOWED_HOSTS تنظیم شود
PostgreSQL استفاده شود
فایل‌های استاتیک/مدیا توسط Nginx سرو شوند
HTTPS فعال شود (Let’s Encrypt)
GitHub Actions برای CI/CD
🤝 مشارکت
Fork کنید
شاخه‌ی جدید بسازید (git checkout -b feature/amazing)
Commit کنید (git commit -m 'Add amazing feature')
Push کنید (git push origin feature/amazing)
Pull Request باز کنید
📄 مجوز
MIT © Sajjad Rezaei
📬 ارتباط
ایمیل: sajjadhosseinrezaei@yahoo.com
لینکدین: linkedin.com/in/sajjadhosseinrezaei
وب‌سایت: sajjadhosseinrezaei.ir
🇬🇧 English
🌟 Features
Fully localized Persian admin
Unlimited project gallery with drag-and-drop ordering
Skill levels 0-100 % + FontAwesome or custom icon
Project status : completed / in-progress / on-hold
Featured flag for skills & projects
Social links stored as flexible JSON
Swagger & ReDoc auto-generated docs
Health-check endpoint for uptime monitoring
Ready for PostgreSQL & Docker
🧰 Tech Stack
Table

Layer	Tech
Backend	Django 4.2 LTS
API	Django REST Framework 3.14
Docs	drf-spectacular (OpenAPI 3)
Storage	Pillow / AWS-S3 / Cloudinary
Database	PostgreSQL (local: SQLite)
Deploy	Gunicorn + Nginx + Docker
⚙️ Quick Start
bash

git clone https://github.com/Sajjadhosseinrezaei/MyWebsite-backend.git
cd MyWebsite-backend

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # fill DB & email settings
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Visit http://localhost:8000/api/schema/swagger-ui/
🔐 Environment Variables (.env)

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
📡 API Endpoints
Table

Method	Endpoint	Description
GET	/api/profile/	Public profile info
GET	/api/skills/	List skills
GET	/api/technologies/	Technologies
GET	/api/project-categories/	Project categories
GET	/api/projects/	All projects
GET	/api/projects/featured/	Featured projects
POST	/api/contact/	Send contact message
GET	/api/health/	Health check
GET	/api/schema/swagger-ui/	Swagger UI
GET	/api/schema/redoc/	ReDoc
🐳 Docker (Production)
bash

docker-compose up -d
Includes: PostgreSQL, web (Django+Gunicorn), Nginx
📸 Screenshots
Table

Admin – Skills	Admin – Projects
docs/skills.png	docs/projects.png
🚢 Deployment Checklist
Set DEBUG=False & strong SECRET_KEY
Run collectstatic
Configure ALLOWED_HOSTS
Use PostgreSQL
Serve static/media via Nginx
Enable HTTPS (Let’s Encrypt)
GitHub Actions for CI/CD
🤝 Contributing
Fork the repo
Create your feature branch (git checkout -b feature/amazing)
Commit (git commit -m 'Add amazing feature')
Push (git push origin feature/amazing)
Open a Pull Request
📄 License
MIT © Sajjad Rezaei
📬 Contact
Email: sajjadhosseinrezaei@yahoo.com
LinkedIn: linkedin.com/in/sajjadhosseinrezaei
Website: sajjadhosseinrezaei.ir
Made with ❤️ in Django
