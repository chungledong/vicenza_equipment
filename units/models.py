from os import name
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class Units(models.Model):

    name = models.CharField(max_length=30,
                            unique=True, null=False, verbose_name="Tên Đvt")
    description = models.TextField(
        null=True, default='Input!..', verbose_name="Mô tả")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Ngày tạo")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Ngày sữa")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    class Meta:
        verbose_name_plural = "Đơn vị tính"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str.lower(self.name)
        # self.validate_unique(self.name)
        return super().save(*args, **kwargs)
