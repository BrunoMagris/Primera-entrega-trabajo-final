from django.db import models

# Create your models here.

class Usuario(models.Model):
    user = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    email = models.EmailField()

class CursosCoderhouse(models.Model):
    categorias = models.CharField(max_length=30)
    cursos = models.CharField(max_length=30)
    duracion = models.CharField(max_length=30)

class CarrerasCoderhouse(models.Model):
    categorias = models.CharField(max_length=30)
    carreras = models.CharField(max_length=30)
    duracion = models.CharField(max_length=30)