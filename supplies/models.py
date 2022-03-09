from django.db import models
from django.shortcuts import reverse
from units.models import Units
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class ItemBase(models.Model):
    # Khai báo lơp Meta để không tạo ra data trong cơ sở dữ liệu
    class Meta:
        abstract = True

    code = models.CharField(_('code'), max_length=30, unique=True, null=False)
    name = models.TextField(_('name'), null=False)
    created_date = models.DateTimeField(_('created_date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated_date'), auto_now=True)
    active = models.BooleanField(_('active'), default=True)

    def __str__(self) -> str:
        return self.name

# Nhóm vật tư


class GroupSupplies(ItemBase):
    description = RichTextField(null=True, verbose_name="Mô tả nhóm vật tư")
    image = models.ImageField(_('image'),
                              upload_to='groupsupplies/%Y/%m', default='No_image.png')

    class Meta:
        verbose_name_plural = "Nhóm vật tư"

    def get_absolute_url(self):
        return reverse("supplies:list-supplies", kwargs={"pk": self.pk})
# Chi tiết vật tư


class Supplies(ItemBase):
    description = RichTextField(null=True, verbose_name="Mô tả vật tư")
    group_supplies = models.ForeignKey(
        GroupSupplies, on_delete=models.SET_NULL, null=True, verbose_name="Nhóm vật tư")
    units = models.ForeignKey(
        Units, on_delete=models.SET_NULL, null=True, verbose_name="Đơn vị tính")
    image = models.ImageField(upload_to='supplies/%Y/%m', default='No_image.png')

    class Meta:
        verbose_name_plural = "Vật tư"
    
    def get_absolute_url(self):
        return reverse("supplies:detail", kwargs={"pk": self.pk})
    
