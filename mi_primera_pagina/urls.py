from django.contrib import admin
from django.urls import path
from AppBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='Inicio'),
    path('profesores/', views.profesores, name='Profesores'),
    path('cursos/', views.cursos, name='Cursos'),
    path('entregables/', views.entregables, name='Entregables'),
    path('buscar/', views.buscar, name='Buscar'),
]
