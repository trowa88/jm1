from rest_framework import viewsets

from comments.models import BuildingComment, BuildingPostComment, BuildingPostCommentLike, BuildingCommentLike
from comments.serializer import BuildingCommentSerializer, BuildingPostCommentSerializer, \
    BuildingPostCommentLikeSerializer, BuildingCommentLikeSerializer


class BuildingCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingCommentSerializer
    queryset = BuildingComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BuildingPostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingPostCommentSerializer
    queryset = BuildingPostComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BuildingPostCommentLikeViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingPostCommentLikeSerializer
    queryset = BuildingPostCommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BuildingCommentLikeViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingCommentLikeSerializer
    queryset = BuildingCommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
