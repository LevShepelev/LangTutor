from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Администрирование модели урока."""
    list_display = ('title', 'created_at')
