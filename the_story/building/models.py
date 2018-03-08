from django.db import models

from core.models import TimeStampedModel


class Building(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='buildings/', default=None)

    def __repr__(self):
        return self.name

    def building_description(self):
        return self.name + ': ' + self.description

    def comment_list(self):
        return self.building_comments.all().values()
