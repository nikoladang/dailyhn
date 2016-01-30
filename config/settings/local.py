from .base import *

DEBUG = True

INSTALLED_APPS += ("debug_toolbar", )

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

STATIC_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/static_in_env"
MEDIA_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/media_in_env"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("POSTGRESQL_NAME"),
        'USER': get_secret("POSTGRESQL_USER"),
        'PASSWORD': get_secret("POSTGRESQL_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}