from django.db import models

# Create your models here.

#Conexión CRUD

#Clase para los edificios
class Locacion(models.Model):
    Nombre = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=100)
    Capacidad_Individual = models.IntegerField(blank = True, null=True)
    Capacidad_Salas = models.IntegerField(blank = True, null=True)
    Servicios_Adicionales = models.CharField(max_length=500)
    Valoracion_Clientes = models.IntegerField(blank = True, null=True)

    def __str__(self):
        return self.Nombre

#Clase para registrar el tipo de lugar entre Sala y Puestos Individuales
class TipoLugar(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(blank = True, null=True)

#Clase para los lugares
class Lugar(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    idTipoLugar = models.ForeignKey(TipoLugar, on_delete=models.CASCADE)
    Capacidad = models.IntegerField(blank = True, null=True)
    Servicios_Adicionales = models.CharField(max_length=500)
    Precio = models.FloatField()
    Disponible = models.BooleanField(blank = True, null=True)

    def __str__(self):
        return self.Capacidad

    def CalcularDisponibilidad(self, Reserva):
        disponibilidad = 0
        if (self.IdLocacion == Reserva.Lugar.IdLocacion) and (self.idTipoLugar == Reserva.Lugar.idTipoLugar):
            if (self.Disponible == True):
                disponibilidad += 1
        return disponibilidad

    def ValidarDisponibilidad(self, Reserva):
        if (self.IdLocacion == Reserva.Lugar.IdLocacion) and (self.idTipoLugar == Reserva.Lugar.idTipoLugar):
            if (self.Disponible == True):
                return self.Disponible
        return False
    
    def ActualizarDisponibilidad(self, Reserva):
        if (self.IdLocacion == Reserva.Lugar.IdLocacion) and (self.idTipoLugar == Reserva.Lugar.idTipoLugar):
            if (self.Disponible == True):
                self.Disponible = False
            else:
                self.Disponible = True
        return True