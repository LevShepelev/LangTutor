from django.db import models

class Lesson(models.Model):
    """
    Модель, представляющая урок по иностранному языку.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
