from decimal import localcontext
from django.shortcuts import render
#Para imprimir mensajes sencillos de respuesta se importa la siguiente libreria:
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict
#from Catalogo.serializers import LocacionSerial, Locacion, TipoLugarSerial, TipoLugar, LugarSerial, Lugar
from Catalogo.serializers import *


class LocacionAPI(viewsets.ModelViewSet):
    serializer_class = LocacionSerial
    queryset = Locacion.objects.all()


class TipoLugarAPI(viewsets.ModelViewSet):
    serializer_class = TipoLugarSerial
    queryset = TipoLugar.objects.all()

class LugarAPI(viewsets.ViewSet):
    def list(self, request):
        lugares = Lugar.objects.all()
        serializador = LugarSerial(lugares, many=True)
        return Response(serializador.data)

    def create(self, request):
        ubicacion = Locacion.objects.get(id = request.data['IdLocacion'])
        ubicacionSerial = LocacionSerial(ubicacion)
        if (request.data['idTipoLugar'] == 1): #Si es un puesto individual, almacena la capacidad máxima de los puestos individuales
            LimitePuestos = ubicacionSerial.data['Capacidad_Individual']
        else: #Si es una sala, almacena la capacidad máxima de las salas
            LimitePuestos = ubicacionSerial.data['Capacidad_Salas']       
        locaciones = get_object_or_404(Locacion, id = request.data['IdLocacion'])
        tipo = get_object_or_404(TipoLugar, id = request.data['idTipoLugar'])
        lugar = Lugar.objects.filter(IdLocacion = locaciones, idTipoLugar = tipo)
        numlugar = len(lugar)
        request.data['num_lugar'] = numlugar + 1
        serializador = LugarSerial(data = request.data)
        if serializador.is_valid():
            if (numlugar < LimitePuestos):
                serializador.save()
                return Response("El lugar se guardó exitosamente")
            else:
                return Response("No es posible crear el puesto, se ha alcanzado el límite máximo")
        return Response(serializador.errors)

    def retrieve(self, request, pk=None):
        # *** pk = 2-3 -> pk1-pk2 / se pasará la llave de manera compuesta ***
        pks = pk.split("-")
        pk1 = pks[0]
        pk2 = pks[1]
        #lugares = Lugar.objects.filter(IdLocacion = pk, idTipoLugar = pk2)
        lugares = Lugar.objects.filter(IdLocacion = pk1)
        tipo = lugares.filter(idTipoLugar = pk2)
        #serializador = LugarSerial(lugares, many = True)
        serializador = LugarSerial(tipo, many = True)
        return Response(serializador.data)



# Create your views here.

def vistaEjemplo(request):
    """
    request -> contiene toda la información del usuario que hace la petición de acceso a la aplicación.  
               A través de métodos GET y POST, principalmente.
    
    GET     -> Método con el cual el usuario solicita acceder a una URL.

    POST    -> Método con el cual el usuario envía información a una URL.

    """
    return HttpResponse ("Hola, estás en la aplicación del catálogo!!!")
