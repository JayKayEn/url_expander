from django import forms
from .models import URLInfo

class URLForm(forms.ModelForm):
    class Meta:
        model = URLInfo
        fields = ('short_url',)
