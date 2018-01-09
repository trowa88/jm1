from rest_framework import viewsets

from building.models import Building
from building.serializer import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing building instances.
    """
    serializer_class = BuildingSerializer
    # queryset = Building.objects.select_related('user').prefetch_related('building_comments',
                                                                        # 'building_comment_likes')
    queryset = Building.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
