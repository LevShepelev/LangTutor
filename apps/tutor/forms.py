"""
Forms for the tutor app.
"""

# pylint: disable=import-error,too-few-public-methods
from django import forms


class ChatForm(forms.Form):
    """Form for sending chat messages."""

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
