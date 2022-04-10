from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'username': 'Login'
        }
        help_texts = {
            'email': 'Informe seu melhor e-mail'
        }
        error_messages = {
            'username': {
                'required': 'Informe um login.'
            }
        }
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.TextInput(attrs={
                'placeholder': '@email.com'
            })
        }
