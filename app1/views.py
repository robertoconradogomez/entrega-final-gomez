from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "app1/inicio.html")

def cursos(request):
    return render(request, "app1/cursos.html")

def estudiantes(request):
    return render(request, "app1/estudiantes.html")

def profesores(request):
    return render(request, "app1/profesores.html")

def entregas(request):
    return render(request, "app1/entregas.html")

def consulta(request):
    return render(request, "app1/consulta.html")