from django.shortcuts import render
from AppFamiliares.models import Familiares

# Create your views here.

def ver_datos(request):
    
    return render(request, "ver_datos.html")

def crear_familiares(request):
    #instanciando modelo
    abuelo = Familiares(nombre="Rene", apellido="Grismado",edad=66,trabaja=False)
    abuela = Familiares(nombre="Alicia", apellido="Larenza",edad=67,trabaja=False)
    hijo = Familiares(nombre="Juan Pablo", apellido="Grismado",edad=15,trabaja=False)
    #guardando los datos en sus respectivas tablas SQL, en una sola linea
    abuelo.save(), abuela.save(), hijo.save()
    #generando parametro para template
    info = {'abuelo':abuelo, 'abuela':abuela, 'hijo':hijo}
    
    return render(request, "crear_familiares.html", info)