from django.shortcuts import render
from gestionTrekking.models import Imagen_galeria

# Create your views here.

def index(request):

    return render(request,"index.html")

def galeria(request):

    images = Imagen_galeria.objects.all()
    print(images)
    

    return render(request,"galeria.html", {'images': images})