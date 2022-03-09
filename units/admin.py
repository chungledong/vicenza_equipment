from django.contrib import admin
from .models import Units
from .forms import UnitsForms
# Register your models here.


class UnitsAdmin(admin.ModelAdmin):
    form = UnitsForms
    list_display = ['name', 'description', 'created_date', 'updated_date']
    search_fields = ['name', 'description', 'created_date', 'updated_date']
    list_filter = ['name', 'created_date', 'updated_date']
    

admin.site.register(Units, UnitsAdmin)
