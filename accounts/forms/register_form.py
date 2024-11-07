###
### Formulario para registrar un nuevo usuario
###
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # Overriding defaults fields

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'input'}))

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'input'}))
    
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'input'}))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'input'}))
    
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'input'}))

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

        widgets = {
            "username":forms.TextInput(attrs={'class':'input'}),
        }