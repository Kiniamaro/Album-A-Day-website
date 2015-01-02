"""
WSGI config for album_A_Day project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "album_A_Day.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
