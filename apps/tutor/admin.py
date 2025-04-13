"""
Admin configuration for the tutor app.
"""

# pylint: disable=import-error,missing-module-docstring,too-few-public-methods

from django.contrib import admin

from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Admin interface for Lesson model."""

    list_display = ("title", "created_at")
