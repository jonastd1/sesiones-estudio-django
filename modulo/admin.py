from django.contrib import admin
from .models import SesionEstudio


@admin.register(SesionEstudio)
class SesionEstudioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'materia', 'fecha', 'duracion_minutos', 'completada', 'usuario')