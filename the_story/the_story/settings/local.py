from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'simple_test_db'
    }
}


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

