from django.db import models
from Catalogo.models import Lugar
from Usuarios.models import Perfil
from datetime import date, datetime

# Create your models here.

#Clase para la Reserva
class Reserva(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, blank=True)
    idLugar = models.ForeignKey(Lugar, on_delete=models.CASCADE,  null=True, blank=True)
    Fecha_ini_reserva = models.DateField(auto_now_add=True)
    Fecha_fin_reserva = models.DateField(auto_now_add=True)
    Pago_confirmado = models.BooleanField(blank = True, null=True)
    Estado_reserva = models.BooleanField(blank = True, null=True)

    def __str__(self):
        return self.usuario.__str__() + ' - ' + self.idLugar.__str__() + ' --> ' + str(self.Fecha_ini_reserva)

    def CancelarReserva(self):
        self.Estado_reserva = False
        return self.Estado_reserva

    def VencimientoReserva(self):
        Fecha_actual = datetime.now
        difFecha = Fecha_actual - self.Fecha_fin_reserva
        if (difFecha >= 0):
            self.Estado_reserva = False
        else:
            self.Estado_reserva = True
        return self.Estado_reserva

#Clase para los pagos
class Pago(models.Model):
    idReserva = models.ForeignKey(Reserva, on_delete=models.CASCADE,  null=True, blank=True)
    Valor_pago = models.FloatField(blank = True, null=True)
    Fecha_pago = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Pago de ' + self.idReserva.usuario.__str__() + ' por ' + self.idReserva.idLugar.__str__() 