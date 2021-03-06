from django.db import models

from core.models import TimeStampedModel


class BuildingPostComment(TimeStampedModel):
    building_post = models.ForeignKey('building.Building',
                                      related_name='building_post_comments',
                                      null=True)
    building_post_comment = models.ForeignKey('self', null=True)
    user = models.ForeignKey('auth.User')
    content = models.CharField(max_length=200)


class BuildingPostCommentLike(TimeStampedModel):
    building_post_comment = models.ForeignKey('BuildingPostComment',
                                              related_name='building_post_comments')
    user = models.ForeignKey('auth.User')

    class Meta:
        unique_together = ('building_post_comment', 'user',)


class BuildingComment(TimeStampedModel):
    building = models.ForeignKey('building.Building',
                                 related_name='building_comments')
    building_comment = models.ForeignKey('self', null=True, default=None)
    user = models.ForeignKey('auth.User')
    content = models.CharField(max_length=200)


class BuildingCommentLike(TimeStampedModel):
    building_comment = models.ForeignKey('BuildingComment',
                                         related_name='building_comment_likes')
    user = models.ForeignKey('auth.User')

    class Meta:
        unique_together = ('building_comment', 'user')
