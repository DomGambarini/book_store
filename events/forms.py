from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'name', 'host', 'duration',
            'event_date', 'event_time',
            'description', 'image']
