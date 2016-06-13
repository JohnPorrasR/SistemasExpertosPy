from django.contrib import admin
from .models import Enfermedad

@admin.register(Enfermedad)
class AdminEnfermedad(admin.ModelAdmin):
    list_display = ('enfermedad_dec', 'enfermedad_val', 'enfermedad_act',)
    list_filter = ('enfermedad_dec',)