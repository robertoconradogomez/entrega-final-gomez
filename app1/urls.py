from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.inicio, name="index"),
    path("cursos/", views.cursos, name="cursos"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("profesores/", views.profesores, name="profesores"),
    path("entregas/", views.entregas, name="entregas"),
    path("buscar/", views.buscar, name="buscar"),
]