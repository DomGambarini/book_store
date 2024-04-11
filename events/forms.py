from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'host', 'date_field', 'time_field', 'description', 'duration', 'image']
