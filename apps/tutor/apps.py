"""
App configuration for the tutor app.
"""

# pylint: disable=import-error,too-few-public-methods
from django.apps import AppConfig


class TutorConfig(AppConfig):
    """Configuration for the tutor app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tutor"
