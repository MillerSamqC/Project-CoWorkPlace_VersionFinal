
from rest_framework import serializers
from Catalogo.models import *

class LocacionSerial(serializers.ModelSerializer):
    class Meta:
        model = Locacion
        fields = '__all__'

class TipoLugarSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoLugar
        fields = '__all__'

class LugarSerial(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class TipoLugarSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoLugar
        fields = '__all__'
