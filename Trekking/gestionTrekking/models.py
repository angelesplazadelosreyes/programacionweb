from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
import os

# Create your models here.

# def cambiar_ruta_de_fichero(instance, filename):
#     if os.path.isdir(os.path.join('uploads', instance.titulo)):
#         pass
#     else:
#         os.mkdir(os.path.join('uploads', instance.titulo))
#     return os.path.join('uploads', instance.titulo , filename)

class Imagen_galeria(models.Model):
    id=models.IntegerField(primary_key = True)
    nombre=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='media')
    fecha=models.DateField()
    lugar=models.CharField(max_length=50)

    def __str__(self):
        return self.lugar

class Banner(models.Model):
    id=models.IntegerField(primary_key = True)
    imagen=models.ImageField(upload_to='media')
    texto=models.CharField(max_length=30)

    def __str__(self):
        return self.texto


class Noticias(models.Model):
    id=models.IntegerField(primary_key = True)
    titulo=models.CharField(max_length=50)
    bajada=models.CharField(max_length=100)
    cuerpo=models.TextField()
    imagen=models.ImageField(upload_to='media')
    fecha=models.DateField()
    estado=models.CharField(max_length=20)
    prioridad=models.CharField(max_length=10)


class Faq(models.Model):
    id=models.IntegerField(primary_key = True)
    titulo=models.CharField(max_length=100)
    cuerpo=models.TextField()
    fecha=models.DateField()
    estado=models.CharField(max_length=20)


class Plantilla(models.Model):
    id=models.IntegerField(primary_key = True)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=12)
    correo=models.EmailField()
    fecha=models.DateField()
    favicon=models.ImageField(upload_to='media')
    logo1=models.ImageField(upload_to='media')
    logo2=models.ImageField(upload_to='media')
    logo3=models.ImageField(upload_to='media')


class Slide(models.Model):
    id=models.IntegerField(primary_key = True)
    slide=models.ImageField(upload_to='media')



