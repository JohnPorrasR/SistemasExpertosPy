from django.db import models
from Tratamiento.models import Tratamiento

class Paciente(models.Model):
    apellido_pat = models.CharField(max_length=255)
    apellido_mat = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    fecha_nac = models.DateTimeField()

    def __str__(self):
        return self.apellido_pat


class Diagnotico(models.Model):
    paciente = models.ForeignKey(Paciente)
    tratamiento = models.ForeignKey(Tratamiento)

    class Meta:
        verbose_name = 'Diagnotico'
        verbose_name_plural = 'Diagnoticos'