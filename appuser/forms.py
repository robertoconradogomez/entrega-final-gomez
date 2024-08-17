from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from appuser.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido.')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Asignar el avatar por defecto
            default_avatar_path = 'avatares/avatar.png'
            Avatar.objects.create(user=user, imagen=default_avatar_path)
        return user

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Email")
    last_name = forms.CharField(label="Apeliido", required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']