from django.contrib import admin
from django.utils.html import mark_safe
from .forms import (
    GroupSuppliesFroms,
    SuppliesForms,
)

from .models import (
    GroupSupplies,
    Supplies,
)


class GroupSuppliesAdmin(admin.ModelAdmin):
    form = GroupSuppliesFroms
    list_display = ['code','name', 
                    'image', 'created_date', 'updated_date']
    search_fields = ['code','name',  'created_date', 'updated_date']
    list_filter = ['code','name', 'created_date', 'updated_date']

    readonly_fields = ['img']

    def img(self, groupsupplies):
        print(groupsupplies.image.name)
        return mark_safe("<img src='/media/{img_url}'  alt='{alt}' width='120px' />".format(img_url=groupsupplies.image.name, alt=groupsupplies.name))


class SuppliesAdmin(admin.ModelAdmin):
    form = SuppliesForms
    list_display = ['code','name','units', 'group_supplies', 'created_date', 'updated_date']
    search_fields = ['code','name', 'units', 'group_supplies', 'created_date', 'updated_date']
    list_filter = ['code','name','units','group_supplies', 'created_date', 'updated_date']

    readonly_fields = ['img']

    def img(self, supplies):
        print(supplies.image.name)
        return mark_safe("<img src='/media/{img_url}'  alt='{alt}' width='120px' />".format(img_url=supplies.image.name, alt=supplies.name))

# Register your models here.


admin.site.register(GroupSupplies, GroupSuppliesAdmin)
admin.site.register(Supplies, SuppliesAdmin)
