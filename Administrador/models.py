from distutils.command.upload import upload
from email.policy import default
from django.db import models
from datetime import datetime
from datetime import timedelta



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
    fecNacimiento=models.DateField(default=datetime.now())
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)


class EstadoSalud(models.Model):
    id=models.IntegerField(primary_key=True)
    #idUsuario=models.ForeignKey(Usuario)
    peso=models.IntegerField(default=0)
    estatura=models.IntegerField(default=0)
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
    tipo=models.CharField(max_length = 10, default='')
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    estado=models.BooleanField(default=True)
    correo=models.EmailField(max_length = 200, default='')
    imagen=models.ImageField(upload_to='Publico', default='Publico/static/Publico/images/new/avatorNR')
    usuario=models.CharField(null=True,blank=True, max_length=50)
    fecha=models.DateField(default=datetime.now())


class Respuesta(models.Model):
    id=models.IntegerField(primary_key=True)
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    estado=models.BooleanField(default=True)
    tipo=models.CharField(max_length = 10, default='')
    imagen=models.ImageField(upload_to='Publico', default='Publico/static/Publico/images/new/avatorNR')
    pregunta=models.ForeignKey(Mensaje,null=True,blank=True,on_delete=models.RESTRICT)
    usuario=models.CharField(null=True,blank=True, max_length=50)
    fecha=models.DateField(default=datetime.now())


class Noticia(models.Model):
    id=models.IntegerField(primary_key=True)
    fecha=models.DateField(auto_now_add=True)
    titulo=models.CharField(max_length = 100, default='')
    bajada=models.CharField(max_length = 400, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    imagen=models.ImageField(upload_to='Publico', default='Publico/static/Publico/images/1.jpg')
    estado=models.BooleanField(default=True)
    prioridad=models.CharField(max_length = 10, default='')


class Galeria(models.Model):
    id=models.IntegerField(primary_key=True)
    imagen=models.ImageField(upload_to='Administrador')
    titulo=models.CharField(max_length = 100, default='')
    url=models.CharField(blank=True, null=True, max_length = 200)
    fecha=models.DateField(auto_now_add=True)
    estado=models.BooleanField(default=True)
    prioridad=models.CharField(max_length = 10, default='')
    esPublico=models.BooleanField(default=False)


class Ruta(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100, default='')
    imagen=models.ImageField(upload_to='Publico')
    descripcion=models.TextField(max_length = 2000, default='')
    dificultad=models.CharField(max_length = 10, default='')
    distancia=models.IntegerField(default=0)
    tiempo=models.DurationField(default=timedelta)
    urlMap=models.CharField(max_length = 200, null=True, blank=True)
    fechaActualizacion=models.DateField(default=datetime.now())
    urlFoto=models.CharField(max_length = 200, null=True, blank=True)


class Salida(models.Model):
    id=models.IntegerField(primary_key=True)
    #idRuta=models.IntegerField
    horaInicio=models.DateTimeField(default=datetime.now())
    precio=models.IntegerField(default=0)
    cupo=models.IntegerField(default=0)
    cupoUsado=models.IntegerField(default=0)
    cupoTraslado=models.IntegerField(default=0)
    cupoTrasladoUsado=models.IntegerField(default=0)
    estado=models.BooleanField(default=True)
    fecha=models.DateField(default=datetime.now())
    lugarEncuentro=models.CharField(max_length = 100, default='')


class Inscripcion(models.Model):
    id=models.IntegerField(primary_key=True)
    #idUsuario=models.IntegerField
    #idSalida=models.IntegerField
    estado=models.BooleanField(default=False)
    fechaPago=models.DateField(default=datetime.now())
    tipoPago=models.CharField(max_length = 20, default='')
    codigoTb=models.CharField(max_length = 50, default='')
    estado=models.BooleanField(default=True)
    tipoDevolucion=models.CharField(max_length = 20, default='')


class Faq(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo=models.CharField(max_length = 100, default='')
    cuerpo=models.TextField(max_length = 1000, default='')
    fecha=models.DateField(auto_now=True)
    estado=models.BooleanField(default=True)
    identificador=models.CharField(max_length = 20, default='')


class Calendario(models.Model):

    id=models.IntegerField(primary_key=True)
    anio=models.CharField(max_length = 20, default='')
    mes=models.CharField(max_length = 20, default='')
    diaInicio=models.CharField(max_length = 20, default='')
    diasMes=models.CharField(max_length = 20, default='')


class Aviso(models.Model):
    id=models.IntegerField(primary_key=True)
    imagen=models.ImageField(upload_to='Administrador')
    descripcion=models.TextField()
    url=models.CharField(max_length = 100, default='')