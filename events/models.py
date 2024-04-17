from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    host = models.CharField(max_length=50)
    duration = models.DurationField(default=timezone.timedelta(hours=1, minutes=30))
    event_date = models.DateField(default=timezone.now, null=False, blank=False)
    event_time = models.TimeField(default=timezone.now().time(), null=False, blank=False)
    description = models.TextField(max_length=4000, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
