from django.urls import path, include
from AppFamiliares.views import *

urlpatterns = [
    path('ver_datos/', ver_datos),
    path('crear_familiares/', crear_familiares)
]