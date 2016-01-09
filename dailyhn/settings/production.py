from .base import *

DEBUG = False

ALLOWED_HOSTS = ["www.dailyhn.com","dailyhn.com","dailyhn.phanthietfood.com","www.dailyhn.phanthietfood.com"]


STATIC_HOST = get_secret("DJANGO_STATIC_HOST")
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT = "/webapps/dailyhn_django/static/"

MEDIA_ROOT = "/webapps/dailyhn_django/media/"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST =get_secret("EMAIL_HOST")
EMAIL_PORT = get_secret("EMAIL_PORT")
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
