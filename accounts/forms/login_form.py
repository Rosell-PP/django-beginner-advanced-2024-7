###
### Formulario para iniciar sesion en la App
###
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    # Overriding defaults fields
    username = UsernameField(widget=forms.TextInput(
        attrs={
                'class':'input',
                'placeholder':"Username",
                'autofocus':True,
            })
        )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':"Password"}))
    