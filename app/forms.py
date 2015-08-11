from django import forms
from django.forms import HiddenInput
from .models import URLInfo

class URLForm(forms.ModelForm):
    class Meta:
        model = URLInfo
        fields = ('short_url',)
