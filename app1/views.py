from django.shortcuts import render
from app1.forms import *
from app1.models import *

def inicio(request):
    return render(request, "app1/inicio.html")

def cursos(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            mi_formulario = CursoFormulario()

    else:
        mi_formulario = CursoFormulario()

    return render(request, "app1/cursos.html", {"mi_formulario": mi_formulario})

def estudiantes(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            nombre = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            nombre.save()
            mi_formulario = EstudianteFormulario()

    else:
        mi_formulario = EstudianteFormulario()

    return render(request, "app1/estudiantes.html", {"mi_formulario": mi_formulario})

def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            nombre = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            nombre.save()
            mi_formulario = ProfesorFormulario()

    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "app1/profesores.html", {"mi_formulario": mi_formulario})

def entregas(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            nombre = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            nombre.save()
            mi_formulario = EntregableFormulario()

    else:
        mi_formulario = EntregableFormulario()

    return render(request, "app1/entregas.html", {"mi_formulario": mi_formulario})

def buscar(request):
    resultados = []
    if request.method == "POST":
        mi_formulario = BuscarFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            comision = informacion.get("comision")

            if comision is not None:
                resultados = Curso.objects.filter(comision=comision)
    else:
        mi_formulario = BuscarFormulario()

    return render(request, "app1/buscar.html", {"mi_formulario": mi_formulario, "resultados": resultados})

