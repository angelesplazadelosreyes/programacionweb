from xml.dom.minidom import Document
from django.urls import path
from Administrador import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('rutas', views.rutas, name="Rutas"),
    path('calendario', views.calendario, name="Calendario"),
    path('galeria', views.galeria, name="Galeria"),
    path('foro', views.foro, name="Foro"),
    path('faq', views.faq, name="Faq"),
    path('noticias', views.noticias, name="Noticias"),
    path('contacto', views.contacto, name="Contacto"),
    path('acceso_registro', views.acceso_registro, name="Acceso_Registro"),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)