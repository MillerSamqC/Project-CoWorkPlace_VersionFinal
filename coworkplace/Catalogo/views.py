from django.shortcuts import render
#Para imprimir mensajes sencillos de respuesta se importa la siguiente libreria:
from django.http import HttpResponse



from rest_framework import viewsets

from Catalogo.serializers import LocacionSerial, Locacion, TipoLugarSerial, TipoLugar, LugarSerial, Lugar


class LocacionAPI(viewsets.ModelViewSet):
    serializer_class = LocacionSerial
    queryset = Locacion.objects.all()


class TipoLugarAPI(viewsets.ModelViewSet):
    serializer_class = TipoLugarSerial
    queryset = TipoLugar.objects.all()


class LugarAPI(viewsets.ModelViewSet):
    serializer_class = LugarSerial
    queryset = Lugar.objects.all()





# Create your views here.

def vistaEjemplo(request):
    """
    request -> contiene toda la información del usuario que hace la petición de acceso a la aplicación.  
               A través de métodos GET y POST, principalmente.
    
    GET     -> Método con el cual el usuario solicita acceder a una URL.

    POST    -> Método con el cual el usuario envía información a una URL.

    """
    return HttpResponse ("Hola, estás en la aplicación del catálogo!!!")
