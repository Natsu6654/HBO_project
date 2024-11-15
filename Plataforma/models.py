from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=60)
    contrasena = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    nombrePelicula = models.CharField(max_length=30)
    ano = models.IntegerField(help_text=1990)
    clasificacion = models.CharField(max_length=6, help_text="+13, +18")
    descripcion = models.CharField(max_length=200)
