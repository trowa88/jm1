from rest_framework import serializers

from comments.models import BuildingPostComment, BuildingComment, BuildingCommentLike, BuildingPostCommentLike
from story_user.serializer import UserSerializer


class BuildingPostCommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = BuildingPostCommentLike
        fields = ('id', 'user')


class BuildingPostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like = BuildingPostCommentLikeSerializer(many=True, read_only=True)

    class Meta:
        model = BuildingPostComment
        fields = ('id', 'user', 'like', 'content', 'created', 'modified')


class BuildingCommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = BuildingCommentLike
        fields = ('id', 'user')


class BuildingCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like = BuildingCommentLikeSerializer(many=True, read_only=True)

    class Meta:
        model = BuildingComment
        fields = ('id', 'user', 'like', 'content', 'created', 'modified')
