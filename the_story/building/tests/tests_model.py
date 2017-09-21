from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from building.models import Building

factory = APIRequestFactory()


class BuildingTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        Building.objects.create(user=self.user, name='A1', description='first building', img=None)
        Building.objects.create(user=self.user, name='A2', description='second building', img=None)

    def test_building_description(self):
        building_a1 = Building.objects.get(name='A1')
        building_a2 = Building.objects.get(name='A2')

        self.assertEqual(building_a1.get_description(), 'A1: first building')
        self.assertEqual(building_a2.get_description(), 'A2: second building')
        self.assertEqual(building_a1.user.username, 'test')
