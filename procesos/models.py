from unittest.util import _MAX_LENGTH
from django.db import models

class Proceso(models.Model):
    juzgado = models.CharField(max_length=30)
    radicado = models.IntegerField()


class Agenda(models.Model):
    cita = models.CharField(max_length=20)
    fecha = models.DateField()

class Nota(models.Model):
    asunto = models.CharField(max_length=20)
    anotacion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.juzgado} | {self.radicado}"
