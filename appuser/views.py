from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout as auth_logout
from appuser.forms import UserRegisterForm
from django.views.generic import View

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


