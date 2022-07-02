from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def inicio(request):

      return render(request, 'Publico/inicio.html')


def rutas(request):

      return render(request, 'Publico/rutas.html')


def calendario(request):

      return render(request, 'Publico/calendario.html')


def galeria(request):

      return render(request, 'Publico/galeria.html')


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