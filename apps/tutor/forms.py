from django import forms


class ChatForm(forms.Form):
    """
    Форма для отправки запроса в чат.
    """

    prompt = forms.CharField(
        label="Введите ваш запрос",
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Напишите что-нибудь для практики языка...",
            }
        ),
        max_length=1000,
    )
