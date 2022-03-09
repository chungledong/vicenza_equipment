from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Units


class UnitsForms(forms.ModelForm):
    class Meta:
        model = Units
        fields = "__all__"