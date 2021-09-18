from django.db import models

# Create your models here.

#Conexión CRUD

#Clase para los edificios
class Locacion(models.Model):
    #IdLocacion = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=100)
    Capacidad_Individual = models.IntegerField()
    Capacidad_Salas = models.IntegerField()
    Servicios_Adicionales = models.CharField(max_length=500)
    Precio = models.FloatField()
    Cantidad_Ind_Disponible = models.IntegerField()
    Cantidad_Ind_Ocupada = models.IntegerField()
    Cantidad_Salas_Disponible = models.IntegerField()
    Cantidad_Salas_Ocupada = models.IntegerField()
    Valoracion_Clientes = models.IntegerField()

#Clase para registrar la renta de puestos individuales
class Puesto_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdPuesto = models.IntegerField()
    Fecha_Renta = models.DateField()

#Clase para registrar la renta de salas
class Sala_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdSala = models.IntegerField()
    Fecha_Renta = models.DateField()

