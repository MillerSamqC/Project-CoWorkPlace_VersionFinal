from  rest_framework import viewsets

from Renta.serializers import ReservaSerial, Reserva, PagoSerial, Pago


class ReservaAPI(viewsets.ModelViewSet):
    serializer_class = ReservaSerial
    queryset = Reserva.objects.all()


class PagoAPI(viewsets.ModelViewSet):
    serializer_class = PagoSerial
    queryset = Pago.objects.all()