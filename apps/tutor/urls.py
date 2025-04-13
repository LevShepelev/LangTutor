"""
URL configuration for the tutor app.
"""

# pylint: disable=import-error,invalid-name
from django.urls import path

from .views import ChatView, HomeView, LessonDetailView

app_name = "tutor"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("lesson/<int:lesson_id>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("chat/<int:lesson_id>/", ChatView.as_view(), name="chat"),
]
