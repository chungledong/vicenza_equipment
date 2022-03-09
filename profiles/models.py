from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no boi...')
    avatar = models.ImageField(
        upload_to='upload_avatar/%Y/%m', default='No_image.png')
    created_date = models.DateTimeField(_('created_date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated_date'), auto_now=True)
    active = models.BooleanField(_('active'),default=True)

    def __str__(self):
        return f"Profile of {self.user.username} "
