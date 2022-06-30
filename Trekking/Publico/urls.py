from django.urls import path
from Publico import views

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