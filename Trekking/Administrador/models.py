from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.db import models
from django.forms import PasswordInput

from Publico.views import rutas

# Create your models here.

class Usuario(models.Model):
    id=models.IntegerField
    idPerfil=models.IntegerField
    correo=models.EmailField(max_length = 200)
    rut=models.CharField(max_length = 10)
    nombres=models.CharField(max_length = 100)
    apellidos=models.CharField(max_length = 100)
    psw=models.CharField(max_length = 100)
    nomUsuario=models.CharField(max_length = 100)
    celular=models.IntegerField
    contactoEmergencia=models.CharField(max_length = 100)
    fonoEmergencia=models.IntegerField
    derivarA=models.CharField(max_length = 100)
    fecNacimiento=models.DateField
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)


class EsadoSalud(models.Model):
    id=models.IntegerField
    idUsuario=id=models.IntegerField
    peso=models.IntegerField
    estatura=models.IntegerField
    probCardiaco=models.CharField
    probPresion=models.CharField
    movilidad=models.CharField
    otrosPob=models.CharField


class Perfil(models.Model):
    id=models.IntegerField
    tipo=models.CharField


class Acceso(models.Model):
    id=models.IntegerField
    idPerfil=models.IntegerField
    idMenu=models.IntegerField


class Menu(models.Model):
    id=models.IntegerField
    nombre=models.CharField
    url=models.CharField


class Menu(models.Model):
    idPerfil=models.IntegerField
    idMenu=models.IntegerField


class Mensaje(models.Model):
    id=models.IntegerField
    idUsuario=models.IntegerField
    tipo=models.CharField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField
    cuerpo=models.TextField
    estado=models.CharField
    correo=models.CharField


class Respuesta(models.Model):
    id=models.IntegerField
    idMensaje=models.IntegerField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField
    cuerpo=models.TextField
    estado=models.CharField
    tipo=models.CharField


class Noticia(models.Model):
    id=models.IntegerField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField
    bajada=models.CharField
    cuerpo=models.TextField
    imagen=models.ImageField
    estado=models.CharField
    prioridad=models.CharField


class Galeria(models.Model):
    id=models.IntegerField
    titulo=models.CharField
    url=models.CharField
    fecha=models.DateField(auto_now_add=True)
    estado=models.CharField
    prioridad=models.CharField
    idPerfil=models.IntegerField


class Ruta(models.Model):
    id=models.IntegerField
    titulo=models.CharField
    descripcion=models.CharField
    dificultad=models.CharField
    distancia=models.IntegerField
    tiempo=models.DurationField
    urlMap=models.CharField
    fechaActualizacion=models.DateField


class Salida(models.Model):
    id=models.IntegerField
    idRuta=models.IntegerField
    horaInicio=models.DateTimeField
    precio=models.IntegerField
    cupo=models.IntegerField
    cupoUsado=models.IntegerField
    cupoTraslado=models.IntegerField
    cupoTrasladoUsado=models.IntegerField
    estado=models.CharField
    fecha=models.DateField
    lugarEncuentro=models.CharField


class Inscripcion(models.Model):
    id=models.IntegerField
    idUsuario=models.IntegerField
    idSalida=models.IntegerField
    estadoPago=models.CharField
    fechaPago=models.DateField
    tipoPago=models.CharField
    codigoTb=models.CharField
    estado=models.CharField
    tipoDevolucion=models.CharField


class Faq(models.Model):
    id=models.IntegerField
    titulo=models.CharField
    cuerpo=models.TextField
    fecha=models.DateField
    estado=models.CharField