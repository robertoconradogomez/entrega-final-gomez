from django.urls import path
from django.contrib.auth.views import LogoutView
from appuser import views

urlpatterns = [
    path ('login/', views.login_request, name="login"),
    path ('register/', views.register, name="register"),
    path ('logout/', LogoutView.as_view(template_name="app1/inicio.html"), name="logout"),
]
