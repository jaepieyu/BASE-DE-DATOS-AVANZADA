from django.db import models
from django.utils.timezone import now
# Create your models here.

class Origen(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "origen"
        verbose_name_plural = "origenes"

class Destino(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "destino"
        verbose_name_plural = "destinos"



class Viajes(models.Model):
    dni = models.CharField(max_length=50, verbose_name="Ingrese Dni")
    ndeplazas = models.CharField(max_length=50, verbose_name="Numero de plazas")
    fecha = models.DateField(default=now, verbose_name="Fecha Actual")
    codigoviaje = models.ForeignKey(Origen,
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
   

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = "viaje"
        verbose_name_plural = " viajes"
