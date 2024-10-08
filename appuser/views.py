from django.shortcuts import render, redirect
from appuser.forms import UserRegisterForm, UserEditForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views  import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.urls import reverse_lazy

#Editar perfil
@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():

            if mi_formulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get('imagen')
                usuario.avatar.save()

            mi_formulario.save()
            return redirect('editarusuario')
    else:
        mi_formulario = UserEditForm(instance=usuario)

    return render(request, "appuser/editarusuario.html", {"form": mi_formulario})

#cambair contraseña
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "appuser/editarcontrasena.html"
    success_url = reverse_lazy("editarusuario")


#Logout
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('login')

#Login    
def login_request(request):

    msg_login = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user:
                login(request, user)
                return render(request, "app1/inicio.html")
            
        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "appuser/login.html", {"form": form, "msg_login": msg_login})


#Crear Usuario
def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            msg_register = "Error en los datos ingresados: " + str(form.errors)

    else:
        form = UserRegisterForm()
    
    return render(request, "appuser/registro.html", {"form": form, "msg_register": msg_register})


