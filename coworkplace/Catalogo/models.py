from django.db import models

# Create your models here.

#Conexión CRUD

#Clase para los edificios
class Locacion(models.Model):
    Nombre = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=100)
    Capacidad_Individual = models.IntegerField()
    Capacidad_Salas = models.IntegerField()
    Servicios_Adicionales = models.CharField(max_length=500)
    Valoracion_Clientes = models.IntegerField()

#Clase para registrar los puestos individuales
class Puesto_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    Capacidad_Individual = models.IntegerField()
    Servicios_Adicionales = models.CharField(max_length=500)
    Precio = models.FloatField()
    Cantidad_Ind_Disponible = models.IntegerField()
    Cantidad_Ind_Ocupada = models.IntegerField()

#Clase para registrar las salas
class Sala_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    Capacidad_Salas = models.IntegerField()
    Servicios_Adicionales = models.CharField(max_length=500)
    Precio = models.FloatField()
    Cantidad_Salas_Disponible = models.IntegerField()
    Cantidad_Salas_Ocupada = models.IntegerField()

#Clase para registrar la renta de los puestos individuales
class Reserva_Puesto_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdPuesto = models.ForeignKey(Puesto_COW, on_delete=models.CASCADE)
    Fecha_Reserva = models.DateField()
    Pago_Confirmado = models.BooleanField()

#Clase para registrar la renta de las salas
class Reserva_Sala_COW(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdSala = models.ForeignKey(Sala_COW, on_delete=models.CASCADE)
    Fecha_Reserva = models.DateField()
    Pago_Confirmado = models.BooleanField()

#Clase para registrar los pagos de las reservas de los puestos
class Pago_Reserva_Puesto(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdPuesto = models.ForeignKey(Puesto_COW, on_delete=models.CASCADE)
    IdReserva = models.ForeignKey(Reserva_Puesto_COW, on_delete=models.CASCADE)
    Valor_Pago = models.FloatField()
    Fecha_Pago = models.DateField()

#Clase para registrar los pagos de las reservas de las salas
class Pago_Reserva_Sala(models.Model):
    IdLocacion = models.ForeignKey(Locacion, on_delete=models.CASCADE)
    IdSala = models.ForeignKey(Sala_COW, on_delete=models.CASCADE)
    IdReserva = models.ForeignKey(Reserva_Sala_COW, on_delete=models.CASCADE)
    Valor_Pago = models.FloatField()
    Fecha_Pago = models.DateField()