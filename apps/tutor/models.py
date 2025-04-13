"""
Models for the tutor app.
"""

# pylint: disable=import-error,too-few-public-methods
from django.db import models


class Lesson(models.Model):
    """Model representing a lesson."""

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ChatSession(models.Model):
    """Model representing a chat session for a lesson."""

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatSession for {self.lesson.title} (ID: {self.id})"


class ChatMessage(models.Model):
    """Model representing a chat message."""

    ROLE_CHOICES = [
        ("system", "System"),
        ("user", "User"),
        ("assistant", "Assistant"),
    ]
    chat_session = models.ForeignKey(
        ChatSession, on_delete=models.CASCADE, related_name="messages"
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
