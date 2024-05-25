from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event']  # You might include additional booking-specific fields if needed

    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('event')
        if event.has_available_seats():
            return cleaned_data
        else:
            raise forms.ValidationError('Event is fully booked. Please try another event.')
