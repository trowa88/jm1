from PIL import Image
from django.urls import reverse
from rest_framework import status

from building.models import Building
from building.serializer import BuildingSerializer
from utils.base import APITestCaseAuthMixin


class GetBuildingsTest(APITestCaseAuthMixin):
    def setUp(self):
        self.test_user, self.auth = self.create_authorization()

        self.a1 = Building.objects.create(user=self.test_user, name='a1', description='first building', img=None)
        self.a2 = Building.objects.create(user=self.test_user, name='a2', description='second building', img=None)
        self.a3 = Building.objects.create(user=self.test_user, name='a3', description='third building', img=None)

    def test_get_all_buildings(self):
        url = reverse('api:building-list')
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_building(self):
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


class CreateNewBuildingTest(APITestCaseAuthMixin):
    def setUp(self):
        self.test_user, self.auth = self.create_authorization()
        self.img_title = '15119855.jpeg'
        self.img = Image.open(self.img_title)
        self.valid_payload = {
            'user': self.test_user,
            'name': 'Test Building',
            'description': 'test create building'
        }
        self.invalid_payload = {
            'user': '',
            'name': '',
            'description': 'test create building'
        }

    def test_create_valid_building(self):
        url = reverse('api:building-list')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth)

        with open(self.img_title, 'rb') as test_img:
            self.valid_payload['img'] = test_img
            response = self.client.post(
                url,
                self.valid_payload,
                format='multipart'
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_building(self):
        url = reverse('api:building-list')
        self.client.credentials(HTTP_AUTHORIZATION=self.auth)
        response = self.client.post(url, self.invalid_payload, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.invalid_payload['user_id'] = 4
        self.invalid_payload['name'] = 'test'
        self.client.post(url, self.invalid_payload, format='multipart')
        building = Building.objects.last()

        self.assertEqual(building.user_id, self.test_user.pk)
