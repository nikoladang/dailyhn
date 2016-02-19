from .base import *

DEBUG = False

ALLOWED_HOSTS = ["www.dailyhn.com","dailyhn.com","dailyhn.phanthietfood.com","www.dailyhn.phanthietfood.com"]

# STATIC_ROOT = "/webapps/dailyhn_django/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =get_secret("EMAIL_HOST")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_USE_TLS = True

# WhiteNoise
STATIC_HOST = get_secret("DJANGO_STATIC_HOST")
STATIC_URL = STATIC_HOST + '/static/'
WHITENOISE_ROOT = os.path.join(BASE_DIR, "../static")