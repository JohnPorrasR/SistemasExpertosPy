from django.db import models

class Sintomas(models.Model):
    sintoma_dec = models.CharField(max_length=255)
    sintoma_val = models.IntegerField()

    class Meta:
        ordering = ('id',)
