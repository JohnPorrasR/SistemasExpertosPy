from django.db import models

class Paciente(models.Model):
    apellido_pat = models.CharField(max_length=255)
    apellido_mat = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dni = models.CharField(max_length=255)
    fecha_nac = models.DateTimeField()
