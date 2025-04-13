import time
from mistralai import Mistral

class MistralAPI:
    """
    Обёртка для работы с Mistral API с использованием пакета `mistralai`.
    Реализует ограничение скорости запросов (не более одного запроса в секунду).
    """
    def __init__(self, api_key: str, rate_limit: float = 1.0) -> None:
        """
        Инициализация клиента Mistral API.

        Args:
            api_key (str): API ключ для доступа к Mistral.
            rate_limit (float): Максимальное число запросов в секунду (по умолчанию 1.0).
        """
        self.llm_model = Mistral(api_key=api_key)
        self.rate_limit = rate_limit
        self.last_request_time = 0

    def _apply_rate_limit(self) -> None:
        """
        Применяет ограничение между запросами к API, чтобы не превышать заданную скорость.
        """
        elapsed = time.time() - self.last_request_time
        min_interval = 1 / self.rate_limit
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

    def chat_complete(self, prompt: str, model: str = "mistral-large-latest", temperature: float = 0.2) -> str:
        """
        Отправляет запрос для завершения чата и получает ответ от модели.

        Args:
            prompt (str): Сообщение пользователя.
            model (str): Идентификатор модели (по умолчанию "mistral-large-latest").
            temperature (float): Параметр, определяющий степень детерминированности ответа.
                                 Низкие значения дают более предсказуемый вывод.

        Returns:
            str: Ответ, сгенерированный моделью Mistral.
        """
        self._apply_rate_limit()
        chat_response = self.llm_model.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        self.last_request_time = time.time()
        answer = chat_response.choices[0].message.content
        return answer

# Пример использования:
if __name__ == "__main__":
    api_key = "H4QoRNAxAOW1o0c9TVY7UIWf9ucZHjiN"
    mistral_api = MistralAPI(api_key=api_key)
    prompt = "Как перевести фразу 'Hello, how are you?' на французский?"
    response = mistral_api.chat_complete(prompt=prompt)
    print("Ответ от Mistral API:", response)
