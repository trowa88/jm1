import json
from datetime import timedelta

from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.urls import reverse
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.settings import oauth2_settings
from rest_framework import status
from rest_framework.test import APITestCase

from building.models import Building
from building.serializer import BuildingSerializer


class BuildingsTest(APITestCase):
    def setUp(self):
        oauth2_settings._SCOPES = ["read", "write"]

        self.test_user = User.objects.create_user("test_user", "test@example.com", "123456")

        self.application = Application.objects.create(
            name="Test Application",
            redirect_uris="http://localhost http://example.com http://example.org",
            user=self.test_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        )

        self.access_token = AccessToken.objects.create(
            user=self.test_user,
            scope="read write",
            expires=timezone.now() + timedelta(seconds=300),
            token="secret-access-token-key",
            application=self.application
        )
        self.auth = self._create_authorization_header(self.access_token.token)
        self.a1 = Building.objects.create(user=self.test_user, name='a1', description='first building', img=None)
        self.a2 = Building.objects.create(user=self.test_user, name='a2', description='second building', img=None)
        self.a3 = Building.objects.create(user=self.test_user, name='a3', description='third building', img=None)

    def _create_authorization_header(self, token):
        return 'Bearer {0}'.format(token)

    def test_get_all_buildings(self):
        url = reverse('api:building-list')
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_signle_building(self):
        url = reverse('api:building-detail', kwargs={'pk': self.a1.pk})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)
        building = Building.objects.get(pk=self.a1.pk)
        serializer = BuildingSerializer(building)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('user'), 'test_user')

    def test_get_invalid_single_building(self):
        url = reverse('api:building-detail', kwargs={'pk': 100})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

