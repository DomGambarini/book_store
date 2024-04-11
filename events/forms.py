from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'host', 'event_datetime', 'description', 'duration', 'image']
