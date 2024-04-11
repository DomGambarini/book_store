from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    host = models.CharField(max_length=50)
    event_datetime = models.DateTimeField(null=False, blank=False)
    description = models.TextField(max_length=4000, null=False, blank=False)
    duration = models.DurationField()
    image = models.ImageField(null=False, blank=False)


    def __str__(self):
        return self.name