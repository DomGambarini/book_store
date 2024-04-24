from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    host = models.CharField(max_length=50)
    duration = models.DurationField(
        null=True, blank=True,
        help_text="Enter duration in the format HH:MM:SS")
    event_date = models.DateField(
        default=timezone.now, null=False, blank=False,
        help_text="Enter date in the format YYYY:MM:DD")
    event_time = models.TimeField(
        default=timezone.now().time(), null=False, blank=False,
        help_text="Enter time in the format of the 24 clock")
    description = models.TextField(max_length=4000, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
