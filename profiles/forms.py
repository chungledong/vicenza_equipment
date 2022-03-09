from dataclasses import fields
from importlib.resources import files
from django import forms
from .models import Profile

class ProfilesForms(forms.ModelForm):
    class Meta:
        model=Profile
        fields = '__all__'