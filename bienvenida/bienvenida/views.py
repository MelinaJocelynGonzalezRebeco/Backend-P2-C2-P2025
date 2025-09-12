from django.http import HttpResponse
from  django.shortcuts import render
from . import models

def inicio(request):
    return HttpResponse("Hola mundo desde Django")


def mostrar_bienvenida(request):
    tu_nombre = "Melina Gonzalez"
    return HttpResponse(f"Bienvenidos a mi primera app Django, {tu_nombre}f")


def lista_productos(request):
    productos =  models.Producto.objects.all()
    return render(request, productos/lista")