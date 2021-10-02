from rest_framework import serializers
from Renta.models import *

class ReservaSerial(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ReservaSerial(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class PagoSerial(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'