from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    detalle = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.nombre
