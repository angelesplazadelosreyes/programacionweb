from cProfile import run
from django.contrib import admin
from Administrador.models import Usuario
from Administrador.models import EstadoSalud
from Administrador.models import Perfil
from Administrador.models import Acceso
from Administrador.models import Menu
from Administrador.models import Mensaje
from Administrador.models import Respuesta
from Administrador.models import Noticia
from Administrador.models import Galeria
from Administrador.models import Ruta
from Administrador.models import Salida
from Administrador.models import Inscripcion
from Administrador.models import Faq
from Administrador.models import Aviso

# Register your models here.

admin.site.register(Usuario)
admin.site.register(EstadoSalud)
admin.site.register(Perfil)
admin.site.register(Acceso)
admin.site.register(Menu)
admin.site.register(Mensaje)
admin.site.register(Respuesta)
admin.site.register(Noticia)
admin.site.register(Galeria)
admin.site.register(Ruta)
admin.site.register(Salida)
admin.site.register(Inscripcion)
admin.site.register(Faq)
admin.site.register(Aviso)