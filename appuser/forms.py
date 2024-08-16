from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido.')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email")
    last_name = forms.CharField(label="Apeliido", required=False)
    first_name = forms.CharField(label="Nombre", required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']