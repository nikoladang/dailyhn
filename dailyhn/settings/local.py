from .base import *

DEBUG = True

INSTALLED_APPS += ("debug_toolbar", )

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/static_in_env"
MEDIA_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/media_in_env"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

