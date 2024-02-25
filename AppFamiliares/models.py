from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    trabaja = models.BooleanField()