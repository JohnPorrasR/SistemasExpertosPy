from django.db import models

class Tratamiento(models.Model):
    tratamiento_desc  = models.CharField(max_length=255)
