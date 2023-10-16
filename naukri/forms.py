from django import forms
from .models import resume

class uploadfileform(forms.ModelForm):
     class Meta:
        model = resume
        fields = ['name', 'cv', 'image']