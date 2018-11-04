from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key =True)
    nombre  =   models.CharField(max_length=30)
    lugar_origen  =   models.CharField(max_length=30)
    ColorPrimerUniforme  =   models.CharField(max_length=30)
    ColorSegundoUniforme =   models.CharField(max_length=30)
    numeroDeJugadores    = models.IntegerField()
    def __str__(self):
        return self.nombre


class Torneo(models.Model):
    id = models.AutoField(primary_key =True)
    nombre    = models.CharField(max_length=60)
    lugar    = models.CharField(max_length=60)
    premio    = models.CharField(max_length=60)
    incripcion  = models.IntegerField()
    equipos   = models.ManyToManyField(Equipo, through='Competicion')
    def __str__(self):
        return self.nombre

class Competicion(models.Model):
    id = models.AutoField(primary_key =True)
    nombre = models.CharField(max_length=60, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    descripcion   = models.CharField(max_length=60, null=True)
    def __str__(self):
        return self.nombre
