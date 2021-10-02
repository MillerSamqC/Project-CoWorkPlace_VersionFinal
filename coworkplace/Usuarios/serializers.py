from rest_framework import serializers
from Usuarios.models import *

class TipoUsuarioReservaSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'

class PerfilReservaSerial(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'