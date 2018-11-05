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
        fields =['nombre', 'lugar', 'premio','incripcion','equipos']
        def __init__ (self, *args, **kwargs):
            super(TorneoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

            self.fields["equipos"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

            self.fields["equipos"].help_text = "Ingrese los Equipos al torneo"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

            self.fields["equipos"].queryset = Equipo.objects.all()
