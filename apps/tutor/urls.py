from django.urls import path
from .views import HomeView, LessonDetailView, ChatView

app_name = 'tutor'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lesson/<int:lesson_id>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('chat/', ChatView.as_view(), name='chat'),
]
