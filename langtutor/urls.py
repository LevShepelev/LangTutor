"""
Project URL configuration for LangTutor.
"""

# pylint: disable=import-error
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.tutor.urls", namespace="tutor")),
]
