from django.urls import path, include               #MEL agrego include
#from Catalogo.views import vistaEjemplo            #MEL queda pendiente ya habia sido realizada en linea 4
from rest_framework.routers import DefaultRouter    #MEL para API´s tipo view set
from Catalogo.views import *                    

#CATALOGO - Aplicacion
router = DefaultRouter()
router.register =('locaciones', LocacionAPI)        
router.register =('lugares', LugarAPI)              
router.register =('tipo_lugares', TipoLugarAPI)     

urlpatterns = [
    #path('ejemplo', vistaEjemplo),
    path('crud/', include(router.urls)) #MEL 
]