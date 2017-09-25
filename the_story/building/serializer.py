from rest_framework import serializers

from building.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Building
        fields = ('user', 'name', 'description', 'img', 'created', 'modified')
