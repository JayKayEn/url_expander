from django import forms
from django.forms import HiddenInput
from .models import URLInfo

class URLForm(forms.ModelForm):
    class Meta:
        model = URLInfo
        fields = ('short_url',)

class URLRemove(forms.ModelForm):
    class Meta:
        model = URLInfo
        fields = '__all__'
        widgets = {
            'short_url': HiddenInput(),
            'expanded_url': HiddenInput(),
            'status_code': HiddenInput(),
            'page_title': HiddenInput(),
        }
