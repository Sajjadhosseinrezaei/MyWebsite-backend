FROM python:3.11-slim

# تنظیم مسیر کاری
WORKDIR /code

# نصب وابستگی‌ها
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کل کد بک‌اند
COPY . /code/

# اجرای گونیکورن
CMD ["gunicorn", "config.wsgi:application", "--bind", "localhost:8000"]
