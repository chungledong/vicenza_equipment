from logging import PlaceHolder
from tkinter import Widget
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    GroupDevice,
    Device,
)


class GroupDeviceForms(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = GroupDevice
        fields = "__all__"

    #def clean_code(self):
        # do something that validates your data
        #return self.cleaned_data["code"]


class DeviceForms(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Device
        fields = "__all__"

    #def clean_code(self):
        # do something that validates your data
        #return self.cleaned_data["code"]
class DeviceSearchForm(forms.Form):
    text_input = forms.CharField(label=False, widget=forms.TextInput(attrs={
        "type":"text",
        "class":"form-control",
        "placeholder":"Nhập thông tin (mã vật tư hoặc tên vật tư) cầm tìm kiếm"
    }))
        