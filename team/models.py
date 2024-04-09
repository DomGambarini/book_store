from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    position = models.CharField(max_length=50, null=False, blank=False)
    bio = models.CharField(max_length=50, null=False, blank=False)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name