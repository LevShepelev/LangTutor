from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.conf import settings
from .forms import ChatForm
from .mistral_api import MistralAPI
from .models import Lesson

# Инициализация клиента Mistral API (в production рекомендуется хранить ключ в переменных окружения)
MISTRAL_API_KEY = 'H4QoRNAxAOW1o0c9TVY7UIWf9ucZHjiN'
mistral_client = MistralAPI(api_key=MISTRAL_API_KEY, rate_limit=settings.MISTRAL_API_RATE_LIMIT)

class HomeView(View):
    """
    Представление домашней страницы, отображающее список уроков.
    """
    def get(self, request):
        lessons = Lesson.objects.all()
        return render(request, 'tutor/home.html', {'lessons': lessons})

class LessonDetailView(View):
    """
    Представление для отображения подробностей урока.
    """
    def get(self, request, lesson_id):
        try:
            lesson = Lesson.objects.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            messages.error(request, "Урок не найден.")
            return redirect('tutor:home')
        return render(request, 'tutor/lesson.html', {'lesson': lesson})

class ChatView(View):
    """
    Представление для чата с языковым помощником.
    """
    def get(self, request):
        form = ChatForm()
        return render(request, 'tutor/chat.html', {'form': form})

    def post(self, request):
        form = ChatForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            try:
                response_text = mistral_client.chat_complete(prompt=prompt)
            except Exception as e:
                response_text = f"Ошибка при обращении к Mistral API: {e}"
            return render(request, 'tutor/chat.html', {'form': form, 'response': response_text})
        return render(request, 'tutor/chat.html', {'form': form})
