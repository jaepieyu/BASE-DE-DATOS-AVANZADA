from django.urls import path
from Apps.viajes.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
