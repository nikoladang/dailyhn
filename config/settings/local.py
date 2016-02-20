from .base import *

DEBUG = True

INSTALLED_APPS += ("debug_toolbar", )

STATIC_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/static_in_env"
MEDIA_ROOT = "/Users/loannguyen/.virtualenv/dailyhn/media_in_env"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("POSTGRESQL_NAME_LOCAL"),
        'USER': get_secret("POSTGRESQL_USER_LOCAL"),
        'PASSWORD': get_secret("POSTGRESQL_PASSWORD_LOCAL"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
