from django.contrib import admin
from django.utils.html import mark_safe
from .models import (
    GroupDevice, 
    Device,
)
from .forms import (
    GroupDeviceForms,
    DeviceForms,
)
# Register your models here.
class GroupDeviceAdmin(admin.ModelAdmin):
    form = GroupDeviceForms
    
    list_display = ['code', 'name', 'image','created_date', 'updated_date']
    search_fields = ['code','name', 'created_date', 'updated_date']
    list_filter = ['code','name', 'created_date', 'updated_date']
    
    readonly_fields = ['img']

    def img(self, groupdevice):
        #print(groupdevice.image.name)
        return mark_safe("<img src='/media/{img_url}'  alt='{alt}' width='120px' />".format(img_url=groupdevice.image.name, alt=groupdevice.name ))

class DeviceAdmin(admin.ModelAdmin):
    form = DeviceForms
    
    list_display = ['code','name','units', 'group_device','created_date', 'updated_date']
    search_fields = ['code','name','units','group_device','supplies', 'created_date', 'updated_date']
    list_filter = ['code','name', 'units', 'group_device','supplies', 'created_date', 'updated_date']
    
    readonly_fields = ['img']

    def img(self, device):
        #print(device.image.name)
        return mark_safe("<img src='/media/{img_url}'  alt='{alt}' width='120px' />".format(img_url=device.image.name, alt=device.name ))

admin.site.register(GroupDevice, GroupDeviceAdmin)
admin.site.register(Device, DeviceAdmin)