#!/usr/bin/env python
import os
import sys
import socket, re

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    if re.match("^192\.168.*$",ip):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyhn.settings.dev_nikola")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyhn.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
