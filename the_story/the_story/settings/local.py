from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [],
#     'DEFAULT_PERMISSION_CLASSES': [],
#     'TEST_REQUEST_DEFAULT_FORMAT': 'json',
# }
