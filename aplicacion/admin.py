from django.contrib import admin
from .models import *

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Torneo, TorneoAdmin)
admin.site.register(Competicion)
# Register your models here.
