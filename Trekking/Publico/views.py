from email.mime import image
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def inicio(request):

      return render(request, 'Publico/inicio.html')


def rutas(request):

      from Administrador.models import Ruta
      ruta = Ruta.objects.all()
      print(ruta)
      

      return render(request, 'Publico/rutas.html', {'ruta':ruta})


def calendario(request):

      return render(request, 'Publico/calendario.html')


def galeria(request):

      from Administrador.models import Galeria
      images = Galeria.objects.all()

      return render(request, 'Publico/galeria.html', {'images': images})

def ruta1(request):
      
      from Administrador.models import Ruta
      ruta = Ruta.objects.all()
      print(ruta)

      return render(request, 'Publico/ruta1.html', {'ruta1': ruta1})

def foro(request):

      return render(request, 'Publico/foro.html')
     

def faq(request):

      from Administrador.models import Faq
      faq = Faq.objects.all()

      return render(request, 'Publico/faq.html', {'faq':faq})


def noticias(request):

      return render(request, 'Publico/noticias.html')


def contacto(request):

      return render(request, 'Publico/contacto.html')

      
def acceso_registro(request):

      return render(request, 'Publico/acceso_registro.html')