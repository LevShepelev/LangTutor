"""
Module tests for the tutor app.
"""

# pylint: disable=invalid-name,missing-function-docstring,import-error

from django.test import Client, TestCase
from django.urls import reverse

from apps.tutor.models import Lesson


class TestTutor(TestCase):
    """
    Test suite for the tutor app views.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.client = Client()
        self.lesson = Lesson.objects.create(
            title="Test Lesson", content="Content of test lesson."
        )

    def test_home_page(self):
        """
        Test that the home page returns a 200 response and contains the lesson title.
        """
        response = self.client.get(reverse("tutor:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lesson.title)

    def test_lesson_detail(self):
        """
        Test that the lesson detail page returns a 200 response and contains the lesson content.
        """
        response = self.client.get(
            reverse("tutor:lesson_detail", args=[self.lesson.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lesson.content)

    def test_chat_view_get(self):
        """
        Test that the chat view returns a 200 response and contains the expected prompt text.
        """
        response = self.client.get(reverse("tutor:chat", args=[self.lesson.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Введите ваш запрос")
