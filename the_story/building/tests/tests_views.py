from PIL import Image
from django.urls import reverse
from rest_framework import status

from building.models import Building
from building.serializer import BuildingSerializer
from comments.models import BuildingComment, BuildingCommentLike
from utils.base import APITestCaseAuthMixin


class GetBuildingsTest(APITestCaseAuthMixin):
    def setUp(self):
        self.test_user, self.auth = self.create_authorization()
        self.a1 = Building.objects.create(user=self.test_user, name='a1', description='first building', img=None)
        self.a2 = Building.objects.create(user=self.test_user, name='a2', description='second building', img=None)
        self.a3 = Building.objects.create(user=self.test_user, name='a3', description='third building', img=None)

        self.b1 = BuildingComment.objects.create(building=self.a1, building_comment=None, user=self.test_user,
                                                 content='first comment')
        self.c1 = BuildingComment.objects.create(building=self.a1, building_comment=self.b1, user=self.test_user,
                                                 content='first comment comment')

        self.d = BuildingCommentLike.objects.create(building_comment=self.b1, user=self.test_user)

    def test_get_all_buildings(self):
        url = reverse('api:building-list')
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        response = self.client.get(url)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_building(self):
        url = reverse('api:building-detail', kwargs={'pk': self.a1.pk})
        response = self.client.get(url)
        building = Building.objects.get(pk=self.a1.pk)
        comment_count = BuildingComment.objects.filter(building=building).count()
        serializer = BuildingSerializer(instance=building)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('user').get('username'), 'test_user')
        self.assertEqual(len(response.data.get('building_comments')), comment_count)

    def test_get_invalid_single_building(self):
        url = reverse('api:building-detail', kwargs={'pk': 100})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBuildingTest(APITestCaseAuthMixin):
    def setUp(self):
        self.test_user, self.auth = self.create_authorization()
        self.img_title = '15119855.jpeg'
        self.img = Image.open(self.img_title)
        self.valid_payload = {
            'name': 'Test Building',
            'description': 'test create building'
        }
        self.invalid_payload = {
            'name': '',
            'description': 'test create building'
        }

    def test_create_valid_building(self):
        url = reverse('api:building-list')

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
        response = self.client.post(url, self.invalid_payload, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
