from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.settings import oauth2_settings
from rest_framework.test import APITestCase, APIClient


class APITestCaseAuthMixin(APITestCase):
    """
    oauth toolkit authorized
    """
    oauth2_settings._SCOPES = ["read", "write"]
    client = APIClient()

    def create_authorization(self):
        test_user = User.objects.create_user("test_user", "test@example.com", "123456")
        self.client.force_authenticate(user=test_user)
        application = Application.objects.create(
            name="Test Application",
            redirect_uris="http://localhost http://example.com http://example.org",
            user=test_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        )

        access_token = AccessToken.objects.create(
            user=test_user,
            scope="read write",
            expires=timezone.now() + timedelta(seconds=300),
            token="secret-access-token-key",
            application=application
        )

        return test_user, 'Bearer {0}'.format(access_token.token)


