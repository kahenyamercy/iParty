from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'campus', 'poster', 'slots', 'budget_amount']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600', 'rows': '5', 'placeholder': 'Event Description'}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600'}),
            'location': forms.TextInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600', 'placeholder': 'Event Location'}),
            'campus': forms.Select(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600'}),
            'poster': forms.FileInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600'}),
            'slots': forms.NumberInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600', 'placeholder': 'Number of Slots'}),
            'budget_amount': forms.NumberInput(attrs={'class': 'w-full border border-gray-300 p-2 rounded focus:outline-blue-600 text-gray-600', 'placeholder': 'Budget Amount'}),
        }
