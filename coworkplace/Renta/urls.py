from django.urls import path, include               # MEL importo
from rest_framework.routers import DefaultRouter    #MEL para API´s tipo view set
from Renta.views import *                           #MEL 

#CATALOGO - Aplicacion
router = DefaultRouter()
router.register =('reservas', ReservaAPI)        #MEL no hay API's aún, por ULM será ReservaAPI
router.register =('pagos', PagoAPI)              #MEL no hay API's aún, por ULM será PagoAPI

urlpatterns = [
    #path('ejemplo', vistaEjemplo),
    path('crud/', include(router.urls)) #MEL 
]