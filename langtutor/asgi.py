"""
ASGI config for LangTutor project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

# pylint: disable=import-error
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langtutor.settings")
application = get_asgi_application()
