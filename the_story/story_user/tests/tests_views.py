from django.contrib.auth.models import User
from django.urls.base import reverse
from rest_framework import status

from utils.base import APITestCaseAuthMixin


class TheStoryUserTest(APITestCaseAuthMixin):
    def setUp(self):
        self.valid_user = {
            'username': 'valid_user',
            'password': 'valid_password',
            'email': 'valid@user.com'
        }
        self.invalid_user = {
            'username': '',
            'password': '',
            'email': 'invalid'
        }

    def test_sign_up_valid_user(self):
        url = reverse('sign_up')
        response = self.client.post(url, self.valid_user, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, User.objects.count())

    def test_sign_up_invalid_user(self):
        url = reverse('sign_up')
        response = self.client.post(url, self.invalid_user, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)