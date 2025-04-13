from django.test import Client, TestCase
from django.urls import reverse

from .models import Lesson


class TutorTests(TestCase):
    """
    Набор базовых тестов для проверки представлений приложения Tutor.
    """

    def setUp(self):
        self.client = Client()
        self.lesson = Lesson.objects.create(
            title="Test Lesson", content="Content of test lesson."
        )

    def test_home_page(self):
        response = self.client.get(reverse("tutor:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lesson.title)

    def test_lesson_detail(self):
        response = self.client.get(
            reverse("tutor:lesson_detail", args=[self.lesson.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lesson.content)

    def test_chat_view_get(self):
        response = self.client.get(reverse("tutor:chat"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Введите ваш запрос")
