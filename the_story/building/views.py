from rest_framework import viewsets

from building.models import Building
from building.serializer import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing building instances.
    """
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
