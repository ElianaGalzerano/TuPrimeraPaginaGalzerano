from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.camada}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - Entregado: {self.entregado}"
