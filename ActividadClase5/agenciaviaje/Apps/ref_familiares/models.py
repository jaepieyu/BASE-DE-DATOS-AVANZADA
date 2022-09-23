from django.db import models

# Create your models here.



# Create your models here.

class Viajes(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "viaje"
        verbose_name_plural = "viajes"


class Ref_familiares(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Ingrese nombre")
    apellidos = models.CharField(max_length=50, verbose_name="ingrese apellidos")
    direccion = models.CharField(max_length=50, verbose_name="ingrese direccion")
    telefono = models.IntegerField(verbose_name="ingrese telefono")
    
    codigoviaje = models.ForeignKey(Viajes,blank=True, on_delete=models.CASCADE)

                               
   

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = "ref familiar"
        verbose_name_plural = " ref familiares"



