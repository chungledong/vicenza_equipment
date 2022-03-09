from pyexpat import model
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    GroupSupplies,
    Supplies,
)


class GroupSuppliesFroms(forms.ModelForm):

    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = GroupSupplies
        fields = "__all__"
 
   

class SuppliesForms(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Supplies
        fields = "__all__"
   
class SuppliesSearchForm(forms.Form):
    text_input = forms.CharField(label=False, widget=forms.TextInput(attrs={
        "type":"text",
        "class":"form-control",
        "placeholder":"Nhập thông tin (mã vật tư hoặc tên vật tư) cầm tìm kiếm"
    }))