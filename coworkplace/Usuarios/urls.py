from django.urls import path, include               #MEL importo
from rest_framework.routers import DefaultRouter    #MEL para API´s tipo view set
from Usuarios.views import *                        #MEL 

#CATALOGO - Aplicacion
router = DefaultRouter()
router.register =('perfiles', PerfilAPI)             #MEL no hay API's aún, por ULM será PerfilAPI
router.register =('tipo_usuarios', TipoUsuarioAPI)   #MEL no hay API's aún, por ULM será Tipo_usuarioAPI

urlpatterns = [
    #path('ejemplo', vistaEjemplo),
    path('crud/', include(router.urls))             #MEL 
]