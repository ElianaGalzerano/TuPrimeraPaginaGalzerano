from django import forms
from .models import Curso, Profesor, Entregable

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

class EntregableFormulario(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado']
