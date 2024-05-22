from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(queryset=None, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'campus', 'phone_number', 'events']
