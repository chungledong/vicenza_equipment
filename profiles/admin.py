from django.contrib import admin
from django.utils.html import mark_safe
from .models import Profile
from .forms import ProfilesForms
# Register your models here.

class ProfilesAdmin(admin.ModelAdmin):
    form = ProfilesForms
    list_display = ['user', 'created_date', 'updated_date']
    search_fields = ['user', 'created_date', 'updated_date']
    list_filter = ['user', 'created_date', 'updated_date']
    readonly_fields = ['avatar_image']

    def avatar_image(self, profiles):
        print(profiles.avatar.name)
        return mark_safe("<img src='/media/{img_url}'  alt='' width='120px' />".format(img_url=profiles.avatar))

admin.site.register(Profile, ProfilesAdmin)