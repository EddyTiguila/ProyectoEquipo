from django import forms
from .models import *

class CompeticionForm(forms.ModelForm):
    class Meta:
        model= Competicion
        fields =['nombre', 'equipo', 'torneo','descripcion',]
class EquipoForm(forms.ModelForm):
    class Meta:
        model= Equipo
        fields =['nombre', 'lugar_origen', 'ColorPrimerUniforme','ColorSegundoUniforme','numeroDeJugadores',]
class TorneoForm(forms.ModelForm):
    class Meta:
        model= Torneo
        fields =['nombre', 'lugar', 'premio','incripcion',]
