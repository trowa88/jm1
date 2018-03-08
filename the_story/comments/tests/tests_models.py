from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from building.models import Building
from comments.models import BuildingComment


class BuildingCommentTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.building = Building.objects.create(user=self.user, name='building', description='first building', img=None)
        BuildingComment.objects.create(building=self.building, user=self.user, content='first comment')
        BuildingComment.objects.create(building=self.building, user=self.user, content='second comment')

    def test_building_comment(self):
        comment_list = self.building.comment_list()
        self.assertEqual(2, len(comment_list))
