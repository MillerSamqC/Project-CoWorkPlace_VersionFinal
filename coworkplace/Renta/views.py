from  rest_framework import viewsets
from rest_framework.response import Response
from Catalogo.serializers import LugarSerial
#from Renta.serializers import ReservaSerial, Reserva, PagoSerial, Pago
from Renta.serializers import *
from rest_framework.decorators import action


class PagoAPI(viewsets.ModelViewSet):
    serializer_class = PagoSerial
    queryset = Pago.objects.all()

#class ReservaAPI(viewsets.ModelViewSet):
#    serializer_class = ReservaSerial
#    queryset = Reserva.objects.all()

class ReservaAPI(viewsets.ViewSet):
    #Consulta solo las reservas activas
    def list(self, request):
        #return Response(request.data['Estado_reserva'])
        reservas = Reserva.objects.all()
        #Reserva.objects.filter(Estado_reserva = request.data['Estado_reserva'])
        serializador = ReservaSerial(reservas, many=True)
        return Response(serializador.data)
    
    #Consulta solo las reservas Activas
    def retrieve(self, request, pk=None):
        #reservas = Reserva.objects.filter(Estado_reserva = request.data['Estado_reserva'])
        pks = pk.split("-")
        pk1 = pks[0]
        pk2 = pks[1]        
        reservas = Reserva.objects.filter(Estado_reserva = pk2)
        serializador = ReservaSerial(reservas, many=True)
        return Response(serializador.data)
    
    #Para crear la reserva, debe validar la disponibilidad del puesto
    def create(self, request):
        puesto = Lugar.objects.get(id = request.data['idLugar'])
        puestoSerial = LugarSerial(puesto)
        disponible = puestoSerial.data['Disponible']
        serializador = ReservaSerial(data = request.data)
        if serializador.is_valid():
            if (disponible == True):
                serializador.save()
                return Response ("La reserva se creó de manera exitosa")
            else:
                return Response ("No fue posible crear la reserva porque el lugar NO se encuentra disponible")
        return Response (serializador.errors)


