import time

from mistralai import Mistral


class MistralAPI:
    """
    Обёртка для работы с Mistral API с использованием пакета `mistralai`.
    Реализует ограничение скорости запросов (не более одного запроса в секунду).
    """

    def __init__(self, api_key: str, rate_limit: float = 1.0) -> None:
        self.llm_model = Mistral(api_key=api_key)
        self.rate_limit = rate_limit
        self.last_request_time = 0

    def _apply_rate_limit(self) -> None:
        """
        Применяет ограничение между запросами, чтобы не превышать заданную скорость.
        """
        elapsed = time.time() - self.last_request_time
        min_interval = 1 / self.rate_limit
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

    def chat_complete(
        self,
        messages: list,
        model: str = "mistral-large-latest",
        temperature: float = 0.2,
    ) -> str:
        """
        Отправляет историю сообщений (список словарей) в Mistral API и возвращает ответ.

        Args:
            messages (list): Список сообщений диалога, где каждое сообщение представлено словарем
                             с ключами "role" и "content".
            model (str): Идентификатор модели, по умолчанию "mistral-large-latest".
            temperature (float): Параметр детерминированности ответа.

        Returns:
            str: Ответ от модели Mistral.
        """
        self._apply_rate_limit()
        chat_response = self.llm_model.chat.complete(
            model=model, messages=messages, temperature=temperature
        )
        self.last_request_time = time.time()
        answer = chat_response.choices[0].message.content
        return answer
