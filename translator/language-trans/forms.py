from django import forms
from .models import *
from django.conf.global_settings import LANGUAGES
 
 
class ImageForm(forms.ModelForm):
    language = LANGUAGES
    to_language = forms.ChoiceField(required=True,choices=language)
    class Meta:
        model = images
        fields = ['image']