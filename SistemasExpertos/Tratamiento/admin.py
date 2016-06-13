from django.contrib import admin
from .models import Tratamiento

@admin.register(Tratamiento)
class AdminProduct(admin.ModelAdmin):
    list_display = ('tratamiento_desc',)
    list_filter = ('tratamiento_desc',)

