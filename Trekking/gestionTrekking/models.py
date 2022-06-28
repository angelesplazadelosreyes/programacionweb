from email.policy import default
from django.db import models
import os

# Create your models here.

def cambiar_ruta_de_fichero(instance, filename):
    if os.path.isdir(os.path.join('uploads', instance.titulo)):
        pass
    else:
        os.mkdir(os.path.join('uploads', instance.titulo))
    return os.path.join('uploads', instance.titulo , filename)

class Imagen_galeria(models.Model):
    nombre=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='media')
    fecha=models.DateField()
    lugar=models.CharField(max_length=50)

    def __str__(self):
        return self.lugar
