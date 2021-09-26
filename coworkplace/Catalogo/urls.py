from django.urls import path
from Catalogo.views import vistaEjemplo

#CATALOGO - Aplicacion

urlpatterns = [
    path('ejemplo', vistaEjemplo),
]