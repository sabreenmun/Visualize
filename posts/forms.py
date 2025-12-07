from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["media", "description"]
        widgets = {
            "media": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "description"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        
        return cleaned_data