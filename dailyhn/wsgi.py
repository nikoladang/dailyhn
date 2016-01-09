"""
WSGI config for dailyhn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import socket, re

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
if re.match("^192\.168.*$",ip):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyhn.settings.dev_nikola")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyhn.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
