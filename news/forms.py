from django import forms
from .models import *


class NewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "description"]
