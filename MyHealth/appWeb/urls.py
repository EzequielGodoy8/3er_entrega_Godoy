
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', Inicio, name=" Home "),
    path('pacientes/', Pacientes, name= "Pacientes"),
    path('profesionales/', Profesionales, name= "Profesionales"),
    path('turnos/', Turnos, name= "Turnos"),
    path ('formulariopaciente/', formulariopaciente, name= "Formulariopaciente" ),
    path ('formularioprofesional/', formularioprofesional, name= "Formularioprofesional" )
]

