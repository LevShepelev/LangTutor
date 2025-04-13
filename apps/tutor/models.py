from django.db import models


class Lesson(models.Model):
    """
    Модель, представляющая урок по предмету.
    """

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ChatSession(models.Model):
    """
    Модель для хранения сессии чата, привязанной к конкретному уроку (предмету).
    """

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # Может хранить идентификатор сессии браузера (если понадобится)
    session_key = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatSession for {self.lesson.title} (ID: {self.id})"


class ChatMessage(models.Model):
    """
    Модель для хранения отдельного сообщения в рамках сессии чата.
    """

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
