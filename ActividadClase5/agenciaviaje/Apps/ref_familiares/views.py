from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("Bienvenidos, Software de viaje - Aplicación Ref_familiares")
