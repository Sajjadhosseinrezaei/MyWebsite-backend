# 1. Base Image
FROM python:3.11-slim

# 2. Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Create and set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy project code
COPY . /app/

# 6. Collect static files
RUN python manage.py collectstatic --no-input

# 7. Define the command to run the application
# !!! "your_project_name" را با نام پوشه پروژه جنگوی خود (همانی که settings.py دارد) عوض کنید !!!
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]