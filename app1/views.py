from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from app1.forms import *
from app1.models import *

class InicioView(TemplateView):
    template_name = "app1/inicio.html"

class AboutView(TemplateView):
    template_name = "app1/about.html"

class CursosListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "app1/cursos.html"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "app1/detallecursos.html"
    context_object_name = "curso"

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = "app1/crearcurso.html"
    fields = ["nombre", "comision", "detalle"]
    success_url = reverse_lazy("cursos")

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "app1/borrar.html"
    success_url = reverse_lazy("cursos") 

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "app1/actualizarcurso.html"
    success_url = reverse_lazy("cursos")
    fields = ["nombre", "comision", "detalle"]