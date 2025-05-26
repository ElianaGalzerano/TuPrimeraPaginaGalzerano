from django.shortcuts import render, redirect
from .forms import CursoFormulario, ProfesorFormulario, EntregableFormulario

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def cursos(request):
    if request.method == "POST":
        form = CursoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = CursoFormulario()
    return render(request, "AppBlog/cursos.html", {"form": form})

def profesores(request):
    if request.method == "POST":
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = ProfesorFormulario()
    return render(request, "AppBlog/profesores.html", {"form": form})

def entregables(request):
    if request.method == "POST":
        form = EntregableFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = EntregableFormulario()
    return render(request, "AppBlog/entregables.html", {"form": form})

from .models import Curso

def buscar(request):
    resultado = None
    if request.GET.get("curso"):
        nombre = request.GET["curso"]
        resultado = Curso.objects.filter(nombre__icontains=nombre)
    return render(request, "AppBlog/buscar.html", {"resultado": resultado})


