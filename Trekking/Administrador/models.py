from django.db import models

from Publico.views import rutas

# Create your models here.

class Usuario(models.Model):
    id=models.IntegerField(primary_key=True)
    idPerfil=models.IntegerField()
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


class EstadoSalud(models.Model):
    id=models.IntegerField(primary_key=True)
    idUsuario=models.ForeignKey(Usuario)
    peso=models.IntegerField()
    estatura=models.IntegerField()
    probCardiaco=models.CharField(max_length = 100)
    probPresion=models.CharField(max_length = 100)
    movilidad=models.CharField(max_length = 100)
    otrosPob=models.CharField(max_length = 100)


class Perfil(models.Model):
    id=models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length = 10)


class Acceso(models.Model):
    id=models.IntegerField(primary_key=True)
    idPerfil=models.ForeignKey(Perfil)
    idMenu=models.IntegerField(max_length = 10)


class Menu(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length = 100)
    url=models.CharField(max_length = 200)


class Mensaje(models.Model):
    id=models.IntegerField(primary_key=True)
    idUsuario=models.IntegerField
    tipo=models.CharField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField
    cuerpo=models.TextField
    estado=models.CharField
    correo=models.CharField


class Respuesta(models.Model):
    id=models.IntegerField(primary_key=True)
    idMensaje=models.IntegerField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100)
    cuerpo=models.TextField(max_length = 1000)
    estado=models.CharField(max_length = 10)
    tipo=models.CharField(max_length = 10)


class Noticia(models.Model):
    id=models.IntegerField(primary_key=True)
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100)
    bajada=models.CharField(max_length = 400)
    cuerpo=models.TextField(max_length = 1000)
    imagen=models.ImageField
    estado=models.CharField(max_length = 10)
    prioridad=models.CharField(max_length = 10)


class Galeria(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100)
    url=models.CharField(max_length = 200)
    fecha=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length = 10)
    prioridad=models.CharField(max_length = 10)
    idPerfil=models.ForeignKey(Perfil)


class Ruta(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100)
    descripcion=models.CharField(max_length = 400)
    dificultad=models.CharField(max_length = 10)
    distancia=models.IntegerField
    tiempo=models.DurationField
    urlMap=models.CharField(max_length = 200)
    fechaActualizacion=models.DateField


class Salida(models.Model):
    id=models.IntegerField(primary_key=True)
    idRuta=models.IntegerField
    horaInicio=models.DateTimeField
    precio=models.IntegerField
    cupo=models.IntegerField
    cupoUsado=models.IntegerField
    cupoTraslado=models.IntegerField
    cupoTrasladoUsado=models.IntegerField
    estado=models.CharField(max_length = 10)
    fecha=models.DateField
    lugarEncuentro=models.CharField(max_length = 100)


class Inscripcion(models.Model):
    id=models.IntegerField(primary_key=True)
    idUsuario=models.IntegerField
    idSalida=models.IntegerField
    estadoPago=models.CharField(max_length = 20)
    fechaPago=models.DateField
    tipoPago=models.CharField(max_length = 20)
    codigoTb=models.CharField(max_length = 50)
    estado=models.CharField(max_length = 10)
    tipoDevolucion=models.CharField


class Faq(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100)
    cuerpo=models.TextField(max_length = 400)
    fecha=models.DateField
    estado=models.CharField(max_length = 10)