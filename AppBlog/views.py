from django.shortcuts import render

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def profesores(request):
    return render(request, "AppBlog/profesores.html")

def cursos(request):
    return render(request, "AppBlog/cursos.html")

def entregables(request):
    return render(request, "AppBlog/entregables.html")

def buscar(request):
    return render(request, "AppBlog/buscar.html")
