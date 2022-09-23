import imp
from django.contrib import admin
from Apps.viajes.models import Viajes

# Register your models here.


class MembershipInline(admin.TabularInline):
    model = Viajes
    extra = 1

admin.site.register(Viajes)
