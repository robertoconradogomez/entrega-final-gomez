from django.urls import path

from app1.views import *

urlpatterns = [
    path("inicio/", inicio),
    path("cursos/", cursos),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("entregas/", entregas),
]