from django.contrib import admin
from django.urls import path, include

#URL BASE DEL PROYECTO => PRINCIPAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('Catalogo.urls')),
    path('renta/', include('Renta.urls')),
    path('usuarios/', include('Usuarios.urls'))
]