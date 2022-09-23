from django.urls import path
from Apps.viajeros.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
