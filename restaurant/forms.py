from django import forms
from datetime import date
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']
        widgets = {
            'booking_date': forms.DateInput(attrs={
                'type': 'date',
                'min': date.today().isoformat()
            }),
            'no_of_guests': forms.NumberInput(attrs={
                'min': 1,
                'max': 20
            })
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < date.today():
            raise forms.ValidationError("You cannot book a date in the past!")
        return booking_date
