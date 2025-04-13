from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views import View

from .forms import ChatForm
from .mistral_api import MistralAPI
from .models import ChatMessage, ChatSession, Lesson

# Инициализация клиента Mistral API
MISTRAL_API_KEY = "H4QoRNAxAOW1o0c9TVY7UIWf9ucZHjiN"
mistral_client = MistralAPI(
    api_key=MISTRAL_API_KEY, rate_limit=settings.MISTRAL_API_RATE_LIMIT
)


class HomeView(View):
    """
    Представление главной страницы, где отображается список уроков.
    """

    def get(self, request):
        lessons = Lesson.objects.all()
        return render(request, "tutor/home.html", {"lessons": lessons})


class LessonDetailView(View):
    """
    Представление страницы с подробным описанием урока.
    """

    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        return render(request, "tutor/lesson.html", {"lesson": lesson})


class ChatView(View):
    """
    Представление для чата с сохранением истории сообщений, привязанной к уроку.
    URL ожидает параметр lesson_id.
    """

    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        # Получаем или создаем сессию чата для данного урока.
        chat_session_id = request.session.get("chat_session_id")
        if chat_session_id:
            try:
                chat_session = ChatSession.objects.get(
                    id=chat_session_id, lesson=lesson
                )
            except ChatSession.DoesNotExist:
                chat_session = ChatSession.objects.create(
                    lesson=lesson, session_key=request.session.session_key
                )
                request.session["chat_session_id"] = chat_session.id
        else:
            chat_session = ChatSession.objects.create(
                lesson=lesson, session_key=request.session.session_key
            )
            request.session["chat_session_id"] = chat_session.id

        messages_history = chat_session.messages.order_by("timestamp")
        form = ChatForm()
        return render(
            request,
            "tutor/chat.html",
            {"form": form, "messages_history": messages_history, "lesson": lesson},
        )

    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        chat_session_id = request.session.get("chat_session_id")
        if chat_session_id:
            try:
                chat_session = ChatSession.objects.get(
                    id=chat_session_id, lesson=lesson
                )
            except ChatSession.DoesNotExist:
                chat_session = ChatSession.objects.create(
                    lesson=lesson, session_key=request.session.session_key
                )
                request.session["chat_session_id"] = chat_session.id
        else:
            chat_session = ChatSession.objects.create(
                lesson=lesson, session_key=request.session.session_key
            )
            request.session["chat_session_id"] = chat_session.id

        form = ChatForm(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data["prompt"]
            # Сохраним сообщение пользователя
            ChatMessage.objects.create(
                chat_session=chat_session, role="user", content=user_prompt
            )

            # Если в сессии еще нет системного сообщения, добавляем его с промптом для выбранного предмета.
            if not chat_session.messages.filter(role="system").exists():
                system_prompt = f"Ты опытный преподаватель по предмету '{lesson.title}'. Отвечай подробно и понятно."
                ChatMessage.objects.create(
                    chat_session=chat_session, role="system", content=system_prompt
                )

            # Собираем историю сообщений для отправки в LLM API
            conversation = []
            for msg in chat_session.messages.order_by("timestamp"):
                conversation.append({"role": msg.role, "content": msg.content})

            try:
                answer = mistral_client.chat_complete(
                    messages=conversation, model="mistral-large-latest", temperature=0.2
                )
            except Exception as e:
                answer = f"Ошибка при обращении к Mistral API: {e}"

            # Сохраняем ответ помощника
            ChatMessage.objects.create(
                chat_session=chat_session, role="assistant", content=answer
            )
            messages_history = chat_session.messages.order_by("timestamp")
            return render(
                request,
                "tutor/chat.html",
                {
                    "form": ChatForm(),
                    "messages_history": messages_history,
                    "lesson": lesson,
                },
            )
        messages_history = chat_session.messages.order_by("timestamp")
        return render(
            request,
            "tutor/chat.html",
            {
                "form": form,
                "messages_history": messages_history,
                "lesson": lesson,
            },
        )
