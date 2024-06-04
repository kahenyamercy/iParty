from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['campus']
        widgets = {
            'campus': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']
