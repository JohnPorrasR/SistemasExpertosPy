from django.contrib import admin
from .models import Paciente, Diagnotico

@admin.register(Paciente)
class AdminPaciente(admin.ModelAdmin):
    list_display = ('apellido_pat', 'apellido_mat', 'nombres', 'email', 'dni', 'fecha_nac',)
    list_filter = ('apellido_pat',)

@admin.register(Diagnotico)
class AdminDiagnotico(admin.ModelAdmin):
    list_display = ('paciente', 'paciente',)
    list_filter = ('tratamiento', 'tratamiento',)
