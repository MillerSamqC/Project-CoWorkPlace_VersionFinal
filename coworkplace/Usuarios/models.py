from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

#Clase para los Usuarios
class TipoUsuario(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre

#Clase para el perfil
class Perfil(models.Model):
    idTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Nombres =  models.CharField(max_length=300)
    Apellidos = models.CharField(max_length=300)
    Direccion = models.CharField(max_length=300)
    Telefono = models.CharField(max_length=100, blank = True, null=True)

    def __str__(self):
        return self.Nombres