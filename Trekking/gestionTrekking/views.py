from turtle import back
from django.shortcuts import render
from gestionTrekking.models import Banner
from gestionTrekking.models import Imagen_galeria
from gestionTrekking.models import Plantilla

# Create your views here.

def index(request):

    banner = Banner.objects.all()

    return render(request,"index.html",{'banner': banner})


def galeria(request):

    images = Imagen_galeria.objects.all()
    banner = Banner.objects.get(id=1)
    

    return render(request,"galeria.html", {'images': images,'banner': banner})


def plantilla(request):

    plantilla = Plantilla.objects.get(id=1)

    return render(request, "plantilla_ppal.html", {'plantilla': plantilla})