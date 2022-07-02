from django.db import models

from Publico.views import rutas

# Create your models here.

class Usuario(models.Model):
    id=models.IntegerField(primary_key=True)
    #idPerfil=models.IntegerField()
    correo=models.EmailField(max_length = 200, default='')
    rut=models.CharField(max_length = 10, default='')
    nombres=models.CharField(max_length = 100, default='')
    apellidos=models.CharField(max_length = 100, default='')
    psw=models.CharField(max_length = 100, default='')
    nomUsuario=models.CharField(max_length = 100)
    celular=models.IntegerField(default=0)
    contactoEmergencia=models.CharField(max_length = 100, default='')
    fonoEmergencia=models.IntegerField(default=0)
    derivarA=models.CharField(max_length = 100, default='')
    fecNacimiento=models.DateField
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)


class EstadoSalud(models.Model):
    id=models.IntegerField(primary_key=True)
    #idUsuario=models.ForeignKey(Usuario)
    peso=models.IntegerField()
    estatura=models.IntegerField()
    probCardiaco=models.CharField(max_length = 100, default='')
    probPresion=models.CharField(max_length = 100, default='')
    movilidad=models.CharField(max_length = 100, default='')
    otrosPob=models.CharField(max_length = 100, default='')


class Perfil(models.Model):
    id=models.IntegerField(primary_key=True)
    tipo=models.CharField(max_length = 10, default='')


class Acceso(models.Model):
    id=models.IntegerField(primary_key=True)
    #idPerfil=models.ForeignKey(Perfil)
    #idMenu=models.IntegerField()


class Menu(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length = 100, default='')
    url=models.CharField(max_length = 200, default='')


class Mensaje(models.Model):
    id=models.IntegerField(primary_key=True)
    #idUsuario=models.IntegerField()
    tipo=models.CharField(max_length = 10, default='')
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    estado=models.CharField(max_length = 10, default='')
    correo=models.CharField(max_length = 200, default='')


class Respuesta(models.Model):
    id=models.IntegerField(primary_key=True)
    idMensaje=models.IntegerField
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    estado=models.CharField(max_length = 10, default='')
    tipo=models.CharField(max_length = 10, default='')


class Noticia(models.Model):
    id=models.IntegerField(primary_key=True)
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    bajada=models.CharField(max_length = 400, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    imagen=models.ImageField
    estado=models.CharField(max_length = 10, default='')
    prioridad=models.CharField(max_length = 10, default='')


class Galeria(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100, default='')
    url=models.CharField(max_length = 200, default='')
    fecha=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length = 10, default='')
    prioridad=models.CharField(max_length = 10, default='')
    #idPerfil=models.ForeignKey(Perfil)


class Ruta(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100, default='')
    descripcion=models.CharField(max_length = 400, default='')
    dificultad=models.CharField(max_length = 10, default='')
    distancia=models.IntegerField
    tiempo=models.DurationField
    urlMap=models.CharField(max_length = 200, default='')
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
    estado=models.CharField(max_length = 10, default='')
    fecha=models.DateField
    lugarEncuentro=models.CharField(max_length = 100, default='')


class Inscripcion(models.Model):
    id=models.IntegerField(primary_key=True)
    idUsuario=models.IntegerField
    idSalida=models.IntegerField
    estadoPago=models.CharField(max_length = 20, default='')
    fechaPago=models.DateField
    tipoPago=models.CharField(max_length = 20, default='')
    codigoTb=models.CharField(max_length = 50, default='')
    estado=models.CharField(max_length = 10, default='')
    tipoDevolucion=models.CharField


class Faq(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    fecha=models.DateField
    estado=models.CharField(max_length = 10, default='')