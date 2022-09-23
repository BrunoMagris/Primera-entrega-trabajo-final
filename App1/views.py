from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from App1.templates import*
from django.template import Template, Context,loader

# Create your views here.

def inicio(request):
    return render(request, "App1/inicio.html")

def padre(request):
    return render(request, "App1/padre.html")

def crearUsuario(request):
    if request.method=="POST":

        formulario1 = CrearUsuario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            
            usuario1 = Usuario(user = info["user"], contraseña = info["contraseña"], email = info["email"])
            
            usuario1.save()

            return render(request, "App1/inicio.html")

    else:
        formulario1 = ()

    return render(request, "App1/formulario1.html", {"form1":formulario1})

def ver_Cursos(request):
    queryset = CursosCoderhouse.objects.all()
    diccionario = {"Cursos":queryset}
    plantilla = loader.get_template("App1/cursos.html")
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)

def ver_Carreras(request):
    queryset = CarrerasCoderhouse.objects.all()
    diccionario = {"Carreras":queryset}
    plantilla = loader.get_template("App1/carreras.html")
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)

def busquedaCursos(request):
    return render(request, "App1/busquedaCursos.html")

def buscar(request):
    if request.GET["categorias"]:
    
        busqueda = request.GET["categorias"]
        cursos = CursosCoderhouse.objects.filter(categorias__icontains=busqueda)

        return render(request, "App1/resultados.html",{"cursos":cursos, "busqueda":busqueda})

    else:
        mensaje = "No enviaste datos"
    return HttpResponse(mensaje)

def busquedaCarreras(request):
    return render(request, "App1/busquedaCarreras.html")

def buscar2(request):
    if request.GET["categorias"]:
    
        busqueda = request.GET["categorias"]
        carreras = CarrerasCoderhouse.objects.filter(categorias__icontains=busqueda)

        return render(request, "App1/resultados2.html",{"carreras":carreras, "busqueda":busqueda})

    else:
        mensaje = "No enviaste datos"
    return HttpResponse(mensaje)