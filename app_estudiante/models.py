
# Create your models here.
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre completo")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")

    def __str__(self):
        return f'{self.nombre} - {self.telefono}'