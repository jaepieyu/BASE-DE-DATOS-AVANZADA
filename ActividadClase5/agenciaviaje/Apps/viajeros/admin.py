from django.contrib import admin
from Apps.viajeros.models import Viajeros

# Register your models here.

class ViajerosADmin(admin.ModelAdmin):
    pass


admin.site.register(Viajeros, ViajerosADmin)
