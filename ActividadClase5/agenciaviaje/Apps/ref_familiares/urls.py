from django.urls import path
from Apps.ref_familiares.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
