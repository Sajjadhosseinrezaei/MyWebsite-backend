from django.db import models


class BaseModel(models.Model):

    """
    بیس مدل برای ساخت فیلد های تاریخ ایجاد و تاریخ اپدیت برای مدل های مورد نیاز
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   