from rest_framework import serializers

from building.models import Building


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Building
        fields = ('url', 'user', 'name', 'description', 'img',
                  'created', 'modified')
