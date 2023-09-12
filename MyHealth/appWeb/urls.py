
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', Inicio, name='Home'),
    path('pacientes/', Pacientes, name= 'Pacientes'),
    path('profesionales/', Profesionales, name= 'Profesionales'),
    path('turnos/', Turnos, name= 'Turnos'),
    path ('formulariopaciente/', formulariopaciente, name= 'Formulariopaciente' ),
    path ('formularioprofesional/', formularioprofesional, name= 'Formularioprofesional' ),
    path ('formularioadquirirturnos/', formularioadquirirturnos, name= 'Formularioadquirirturnos' ),
    path ('busquedapacientes/', busquedapacientes, name= 'Busquedapacientes' ),
    path ('buscarpacientes/', buscarpacientes, name= 'Buscarpacientes' ),
    path ('consultarturnos/', Consultarturnos, name= 'Consultarturnos' ),


]

