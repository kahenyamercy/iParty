from django import forms
from .models import Campus

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['name', 'location', 'initials']
