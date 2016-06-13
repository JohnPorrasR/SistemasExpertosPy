from django.db import models

class Enfermedad(models.Model):
    enfermedad_dec = models.CharField(max_length=255)
    enfermedad_val = models.IntegerField(unique=True)
    enfermedad_act = models.IntegerField()

    class Meta:
        ordering = ('id',)
