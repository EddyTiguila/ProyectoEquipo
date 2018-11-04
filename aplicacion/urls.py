from django.conf.urls import url
from .views import *
urlpatterns =[
url(r'^$',home, name ="index"),
url(r'^crear_competicion/',crearCompeticion, name ="CrearCompeticion"),
url(r'^crear_equipo/',crearEquipo, name ="CrearEquipo"),
url(r'^crear_torneo/',crearTorneo, name ="CreaTorneo"),
url(r'^listar_competicion/',listarCompeticion, name="listar_competicion"),
url(r'^listar_equipo/',listarEquipo, name="listar_equipo"),
url(r'^listar_torneo/',listarTorneo, name="listar_torneo"),
url(r'^editar_competicion/(?P<id>\d+)/$',editarCompeticion, name="editar_competicion"),
url(r'^editar_equipo/(?P<id>\d+)/$',editarEquipo, name="editar_equipo"),
url(r'^editar_torneo/(?P<id>\d+)/$',editarTorneo, name="editar_torneo"),
url(r'^eliminar_competicion/(?P<id>\d+)/$',eliminarCompeticion, name="eliminar_competicion"),
url(r'^eliminar_equipo/(?P<id>\d+)/$',eliminarEquipo, name="eliminar_equipo"),
url(r'^eliminar_torneo/(?P<id>\d+)/$',eliminarTorneo, name="eliminar_torneo"),
]
