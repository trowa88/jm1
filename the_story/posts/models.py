from django.db import models

from core.models import TimeStampedModel


class BuildingPost(TimeStampedModel):
    building = models.ForeignKey('building.Building',
                                 related_name='building_posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey('auth.User')


class BuildingPostLike(TimeStampedModel):
    building_post = models.ForeignKey('BuildingPost',
                                      related_name='building_posts_likes')
    user = models.ForeignKey('auth.User')
