from tempus_dominus.widgets import DateTimePicker
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Class to construct booking form from the model.
    """
