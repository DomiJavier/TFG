from django.contrib import admin
from django.urls import path, include
from tfg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funciona/', funciona),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', calendario, name='calendario'),
    path('evento', evento, name='evento'),
    path('salir/', salir, name='salir'),
    path('registro/', registro, name='registro'),
    path('registrar/', registrar, name='registrar'),
    path('perfil/', perfil, name='perfil'),
    path('perfilM/', perfilM, name='perfilM'),
    path('crearDatos/', crearDatos, name='crearDatos'),
]
