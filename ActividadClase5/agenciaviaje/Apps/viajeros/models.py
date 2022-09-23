from django.db import models

from django.contrib.auth.models import User


class Viajeros(models.Model):
    nombreViajeros = models.CharField(max_length=100, help_text="Ingrese el Nombre del viajero")
    direccionViajeros = models.CharField(max_length=100, help_text="Ingrese la Direccion del viajero")
    telefonoViajeros = models.CharField(max_length=12, help_text="Ingrese el Telefono del viajero")
    usuario= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    

    def __str__(self):
        return self.nombreViajeros

    class Meta:
        verbose_name = "viaje"
        verbose_name_plural = "viajero"
