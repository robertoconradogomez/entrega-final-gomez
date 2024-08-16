from django.urls import path
from appuser.views import CustomLogoutView
from appuser import views


urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('editarusuario/', views.editar_perfil, name="editarusuario"),
    path('editarcontrasena/', views.CambiarContrasenia.as_view(), name="editarcontrasena"),
]