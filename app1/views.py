from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app1.forms import *
from app1.models import *

class InicioView(TemplateView):
    template_name = "app1/inicio.html"

class CursosListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "app1/cursos.html"

class CursoCreateView(CreateView):
    model = Curso
    template_name = "app1/crearcurso.html"
    fields = ["nombre", "comision"]
    success_url = reverse_lazy("cursos")

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "app1/borrar.html"
    success_url = reverse_lazy("cursos") 

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "app1/actualizarcurso.html"
    success_url = reverse_lazy("cursos")
    fields = ["nombre", "comision"]

class EstudiantesView(FormView):
    template_name = "app1/estudiantes.html"
    form_class = EstudianteFormulario
    success_url = reverse_lazy('estudiantes')

    def form_valid(self, form):
        informacion = form.cleaned_data
        estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
        estudiante.save()
        return super().form_valid(form)

class ProfesoresView(FormView):
    template_name = "app1/profesores.html"
    form_class = ProfesorFormulario
    success_url = reverse_lazy('profesores')

    def form_valid(self, form):
        informacion = form.cleaned_data
        profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
        profesor.save()
        return super().form_valid(form)

class EntregasView(FormView):
    template_name = "app1/entregas.html"
    form_class = EntregableFormulario
    success_url = reverse_lazy('entregas')

    def form_valid(self, form):
        informacion = form.cleaned_data
        entregable = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
        entregable.save()
        return super().form_valid(form)

class BuscarView(FormView):
    template_name = "app1/buscar.html"
    form_class = BuscarFormulario

    def form_valid(self, form):
        informacion = form.cleaned_data
        comision = informacion.get("comision")
        resultados = []

        if comision is not None:
            resultados = Curso.objects.filter(comision=comision)

        return self.render_to_response(self.get_context_data(resultados=resultados, form=form))

