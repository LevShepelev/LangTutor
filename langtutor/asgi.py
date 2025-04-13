"""
ASGI config for LangTutor project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "langtutor.settings")
application = get_asgi_application()
