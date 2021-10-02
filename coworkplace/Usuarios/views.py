from rest_framework import viewsets

from Usuarios.serializers import PerfilSerial, TipoUsuarioSerial, TipoUsuario, Perfil

class TipoUsuarioAPI(viewsets.ModelViewSet):
    serializer_class = TipoUsuarioSerial
    queryset = TipoUsuario.objects.all()


class PerfilAPI(viewsets.ModelViewSet):
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()