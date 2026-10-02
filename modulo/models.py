from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class SesionEstudio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sesiones')
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=60)
    fecha = models.DateField()
    duracion_minutos = models.PositiveIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(600)]
    )
    completada = models.BooleanField(default=False)
    notas = models.TextField(blank=True)

    class Meta:
        ordering = ['-fecha', '-id']

    def clean(self):
        if self.fecha and self.fecha > timezone.localdate():
            raise ValidationError({'fecha': 'La fecha no puede ser futura.'})

    def __str__(self):
        return f'{self.titulo} - {self.materia}'