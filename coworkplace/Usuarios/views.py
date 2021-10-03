from rest_framework import viewsets

from Usuarios.serializers import PerfilReservaSerial, TipoUsuarioReservaSerial, TipoUsuario, Perfil

class TipoUsuarioAPI(viewsets.ModelViewSet):
    serializer_class = TipoUsuarioReservaSerial
    queryset = TipoUsuario.objects.all()


class PerfilAPI(viewsets.ModelViewSet):
    serializer_class = PerfilReservaSerial
    queryset = Perfil.objects.all()