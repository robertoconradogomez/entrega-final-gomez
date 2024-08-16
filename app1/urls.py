from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.InicioView.as_view(), name="index"),
    path("cursos/", views.CursosListView.as_view(), name="cursos"),
    path("crearcurso/", views.CursoCreateView.as_view(), name="crearcurso"),
    path("curso/<int:pk>/", views.CursoDetailView.as_view(), name="detallecursos"),
    path("actualizarcurso/<pk>", views.CursoUpdateView.as_view(), name="actualizarcurso"),
    path("borrar/<pk>", views.CursoDeleteView.as_view(), name="borrarcurso"),
    path("about", views.AboutView.as_view(), name="about"),
]