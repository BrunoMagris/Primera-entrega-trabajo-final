from django.urls import path

from App1.views import *

urlpatterns = [
    path("padre/",padre),
    path("",inicio, name='Inicio'),
    path("form1/", crearUsuario, name='Registrarse'),
    path("cursos/",ver_Cursos, name='Cursos'),
    path("carreras/", ver_Carreras, name='Carreras'),
    path("buscarCursos/", busquedaCursos, name='BuscarCu'),
    path("buscarCu/", buscar),
    path("buscarCarreras/", busquedaCarreras, name='BuscarCa'),
    path("buscarCa/", buscar2),
]