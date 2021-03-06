from django.shortcuts import render, redirect
from .models import *
from .forms import CompeticionForm
from .forms import EquipoForm
from .forms import TorneoForm
from django.contrib import messages

def home (request):
    return render(request, 'index.html')

def crearCompeticion(request):
    if request.method =='POST':
        form=CompeticionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_competicion')
    else:
        form =CompeticionForm()
        return render(request,'aplicacion/crear_competicion.html', {'form':form})

def crearEquipo(request):
    if request.method =='POST':
        form=EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_equipo')
    else:
        form =EquipoForm()
        return render(request,'aplicacion/crear_equipo.html', {'form':form})
def crearTorneo(request):
    if request.method == "POST":

        formulario = TorneoForm(request.POST)

        if formulario.is_valid():

            torneo = Torneo.objects.create(nombre=formulario.cleaned_data['nombre'], lugar = formulario.cleaned_data['lugar'], premio=formulario.cleaned_data['premio'], incripcion=formulario.cleaned_data['incripcion'])

            for equipo_id in request.POST.getlist('equipos'):

                competicion = Competicion(nombre='--',equipo_id=equipo_id, torneo_id= torneo.id, descripcion='--')

                competicion.save()

            messages.add_message(request, messages.SUCCESS, 'Torneo Guardado Exitosamente')
            return redirect('listar_torneo')

    else:

        formulario = TorneoForm()

    return render(request, 'aplicacion/crear_torneo.html', {'formulario': formulario})

def listarCompeticion(request):
    competicion = Competicion.objects.all()
    context = {'competicion':competicion}
    return render (request, 'aplicacion/listar_competicion.html', context)
def listarEquipo(request):
    equipo = Equipo.objects.all()
    context = {'equipo':equipo}
    return render (request, 'aplicacion/listar_equipo.html', context)
def listarTorneo(request):
    torneo = Torneo.objects.all()
    context = {'torneo':torneo}
    return render (request, 'aplicacion/listar_torneo.html', context)
def editarCompeticion (request, id):
    competicion=Competicion.objects.get(id=id)
    if request.method =='GET':
        form =CompeticionForm(instance=competicion)
    else:
        form = CompeticionForm(request.POST, instance = competicion)
        if form.is_valid():
            form.save()
        return redirect ('listar_competicion')
    return render(request, 'aplicacion/crear_competicion.html', {'form':form})
def editarEquipo (request, id):
    equipo=Equipo.objects.get(id=id)
    if request.method =='GET':
        form =EquipoForm(instance=equipo)
    else:
        form = EquipoForm(request.POST, instance = equipo)
        if form.is_valid():
            form.save()
        return redirect ('listar_equipo')
    return render(request, 'aplicacion/crear_equipo.html', {'form':form})

def editarTorneo (request, id):
    torneo=Torneo.objects.get(id=id)
    if request.method =='GET':
        formulario =TorneoForm(instance=torneo)
    else:
        formulario = TorneoForm(request.POST, instance = torneo)
        if formulario.is_valid():
            Torneo.objects.filter(id=id).update(nombre=formulario.cleaned_data['nombre'], lugar = formulario.cleaned_data['lugar'], premio=formulario.cleaned_data['premio'], incripcion=formulario.cleaned_data['incripcion'])

            for equipo_id in request.POST.getlist('equipos'):

                Competicion.objects.filter(id=id).update(nombre='--',equipo_id=equipo_id, torneo_id= torneo.id, descripcion='--')



            messages.add_message(request, messages.SUCCESS, 'Torneo Guardado Exitosamente')
        return redirect ('listar_torneo')
    return render(request, 'aplicacion/crear_torneo.html', {'formulario':formulario})


def eliminarCompeticion (request, id):
    competicion = Competicion.objects.get(id=id)
    if request.method =='POST':
        competicion.delete()
        return redirect('listar_competicion')
    return render (request, 'aplicacion/eliminar_competicion.html', {'competicion':competicion})

def eliminarEquipo (request, id):
    equipo = Equipo.objects.get(id=id)
    if request.method =='POST':
        equipo.delete()
        return redirect('listar_equipo')
    return render (request, 'aplicacion/eliminar_equipo.html', {'equipo':equipo})

def eliminarTorneo (request, id):
    torneo = Torneo.objects.get(id=id)
    if request.method =='POST':
        torneo.delete()
        return redirect('listar_torneo')
    return render (request, 'aplicacion/eliminar_torneo.html', {'torneo':torneo})
# Create your views here.
