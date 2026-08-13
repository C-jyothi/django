from django import forms
from django.core.exceptions import ValidationError


def validate_not_gmail(value):
    if value.endswith('@gmail.com'):
        raise ValidationError("Gmail is not allowed.")


class LoginForm(forms.Form):

    email = forms.EmailField(
        validators=[validate_not_gmail]
    )

    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput
    )