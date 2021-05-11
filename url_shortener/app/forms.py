from django import forms
from .models import Url

class GenerateUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original']