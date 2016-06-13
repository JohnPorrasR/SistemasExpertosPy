from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class AdminProduct(admin.ModelAdmin):
    list_display = ('apellido_pat', 'apellido_mat', 'nombres', 'email', 'dni', 'fecha_nac',)
    list_filter = ('apellido_pat',)
