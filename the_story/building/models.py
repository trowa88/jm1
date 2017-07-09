from django.db import models

from core.models import TimeStampedModel


class Building(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='building/')