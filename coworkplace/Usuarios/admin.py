from django.contrib import admin

from Usuarios.models import TipoUsuario, Perfil

admin.site.register(TipoUsuario)
admin.site.register(Perfil)