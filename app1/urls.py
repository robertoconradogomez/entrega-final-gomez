from django.urls import path

from app1.views import *

urlpatterns = [
    path("", inicio, name="index"),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregas/", entregas, name="entregas"),
    path("consulta/", consulta, name="consultas"),
]