from django import forms
from .models import SesionEstudio


class SesionForm(forms.ModelForm):
    class Meta:
        model = SesionEstudio
        fields = ['titulo', 'materia', 'fecha', 'duracion_minutos', 'completada', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }