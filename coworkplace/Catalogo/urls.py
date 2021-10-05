from django.urls import path, include               #MEL agrego include
#from Catalogo.views import vistaEjemplo            #MEL queda pendiente ya habia sido realizada en linea 4
from rest_framework.routers import DefaultRouter    #MEL para API´s tipo view set
from Catalogo.views import *                    

#CATALOGO - Aplicacion
router = DefaultRouter()
router.register('locaciones', LocacionAPI, basename="Locacion")        
router.register('lugares', LugarAPI, basename="Lugar")              
router.register('tipo_lugares', TipoLugarAPI, basename="TipoLugar")     

urlpatterns = [
    #path('ejemplo', vistaEjemplo),
    path('crud/', include(router.urls)) #MEL 
]