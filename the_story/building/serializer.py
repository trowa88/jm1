from rest_framework import serializers

from building.models import Building
from comments.serializer import BuildingCommentSerializer, BuildingCommentLikeSerializer
from story_user.serializer import UserSerializer


class BuildingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    building_comments = BuildingCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('id', 'user', 'building_comments', 'name',
                  'description', 'img', 'created', 'modified')
