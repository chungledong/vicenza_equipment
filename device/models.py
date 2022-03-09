from django.db import models
from django.shortcuts import reverse
from units.models import Units
from supplies.models import Supplies
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
        return f"{self.code} - {self.name}"

# Nhóm thiết bị máy móc


class GroupDevice(ItemBase):
    description = RichTextField(_('description'), null=True)
    image = models.ImageField(_('image'),
                              upload_to='groupdevice/%Y/%m', default='No_image.png')

    class Meta:
        verbose_name_plural = "Nhóm thiết bị"

    '''
    Hàm gọi trả về danh sách thiết bị the khóa id của nhóm thiết bị
    
    '''

    def get_absolute_url(self):
        return reverse("device:list-device", kwargs={"pk": self.pk})
# Thiết bị máy móc


class Device(ItemBase):
    description = RichTextField(_('description'), null=True)
    group_device = models.ForeignKey(
        GroupDevice, on_delete=models.SET_NULL, null=True)
    units = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)
    supplies = models.ManyToManyField(Supplies)
    image = models.ImageField(
        _('image'), upload_to='device/%Y/%m', default='No_image.png')

    class Meta:
        verbose_name_plural = "Thiết bị"

    def get_absolute_url(self):
        return reverse("device:list-supplies", kwargs={"pk": self.pk})
