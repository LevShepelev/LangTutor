"""
WSGI config for LangTutor project.
"""

# pylint: disable=import-error
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langtutor.settings")
application = get_wsgi_application()
