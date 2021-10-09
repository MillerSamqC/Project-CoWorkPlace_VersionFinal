from django.contrib import admin
from django.urls import path, include
from .views import LandingPage, Registro, Reserva, Acerca, Contactos, ReservaUser

#Importar contenido estático (imágenes, archivos pdf, css, html, etc...)
from django.conf.urls.static import static
from django.conf import settings
#URL BASE DEL PROYECTO => PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('Catalogo.urls')),
    path('renta/', include('Renta.urls')),
    path('usuarios/', include('Usuarios.urls')),
    path('', LandingPage.as_view()),
    path('registro/', Registro.as_view()),
    path('reserva/', Reserva.as_view()),
    path('acerca/', Acerca.as_view()),
    path('contactos/', Contactos.as_view()),
    path('reservauser/', ReservaUser.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)