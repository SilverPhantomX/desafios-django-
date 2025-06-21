from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(request):
    return HttpResponse("hola desde django, este es un mensaje fijo")
    
def saludo_nombre(request,nombre):
    return HttpResponse(f"hola {nombre}")

def edad(request,edad):
    return HttpResponse(f"tienes {edad}")
