from django.contrib import admin
from .models import Sintomas

@admin.register(Sintomas)
class AdminSintomas(admin.ModelAdmin):
    list_display = ('sintoma_dec', 'sintoma_val',)
    list_filter = ('sintoma_dec',)
