from django.urls import path
from app1.views import *

urlpatterns = [
    path("", InicioView.as_view(), name="index"),
    path("cursos/", CursosListView.as_view(), name="cursos"),
    path("estudiantes/", EstudiantesView.as_view(), name="estudiantes"),
    path("profesores/", ProfesoresView.as_view(), name="profesores"),
    path("entregas/", EntregasView.as_view(), name="entregas"),
    path("buscar/", BuscarView.as_view(), name="buscar"),
    path("crearcurso/", CursoCreateView.as_view(), name="crearcurso"),
    path("actualizarcurso/<pk>", CursoUpdateView.as_view(), name="actualizarcurso"),
    path("borrar/<pk>", CursoDeleteView.as_view(), name="borrarcurso"),
]