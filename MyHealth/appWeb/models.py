from django.db import models
from django import forms

# Create your models here.

class paciente (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    DNI = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField (null=True, blank=True)
    direccion = models.CharField (max_length=150)
    Nro_telefono = models.IntegerField ()
    ocupacion = models.CharField (max_length=50)
    
class Profesional_salud (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField (max_length=50)
    Nro_telefono = models.IntegerField(null=True, blank=True)
    nro_matricula = models.IntegerField ()
    especialidad = models.CharField(max_length=50)
    
class Turnos (models.Model):
    FECHA_CHOICES = [
        ('2023-09-10', '10 de Septiembre de 2023'),
        ('2023-09-11', '11 de Septiembre de 2023'),
        ('2023-09-12', '12 de Septiembre de 2023'),
        ('2023-09-13', '13 de Septiembre de 2023'),
        ('2023-09-14', '14 de Septiembre de 2023'),
        ('2023-09-15', '15 de Septiembre de 2023'),
        ('2023-09-16', '16 de Septiembre de 2023'),
        ('2023-09-17', '17 de Septiembre de 2023'),
        ('2023-09-18', '18 de Septiembre de 2023'),
        ('2023-09-19', '19 de Septiembre de 2023'),
        ('2023-09-20', '20 de Septiembre de 2023'),
        ('2023-09-21', '21 de Septiembre de 2023'),
        ('2023-09-22', '22 de Septiembre de 2023'),
        ('2023-09-23', '23 de Septiembre de 2023'),
        ('2023-09-24', '24 de Septiembre de 2023'),
        ('2023-09-25', '25 de Septiembre de 2023'),
        ('2023-09-26', '26 de Septiembre de 2023'),
        ('2023-09-27', '27 de Septiembre de 2023'),
        ('2023-09-28', '28 de Septiembre de 2023'),
        ('2023-09-29', '29 de Septiembre de 2023'),
        ('2023-09-30', '30 de Septiembre de 2023'),
        ('2023-10-01', '1 de octubre de 2023'),
    ]
    HORARIOS_CHOICES =[
        ('09:00', '9:00 AM'),
        ('09:30', '9:30 AM'),
        ('10:00', '10:00 AM'),
        ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('12:00', '12:00 AM'),
        ('12:30', '12:30 AM'),
    ]
    horario = models.CharField (max_length=5, null=False, choices= HORARIOS_CHOICES)
    fecha = models.CharField (max_length=10, null=False, choices= FECHA_CHOICES)
    paciente = models.ForeignKey (paciente, on_delete =models.CASCADE)
    profesional = models.ForeignKey (Profesional_salud, on_delete =models.CASCADE)

class Turnospaciente (models.Model):
    paciente = models.ForeignKey (paciente, on_delete =models.CASCADE )
    turnos_Adquiridos = models.ManyToManyField (Turnos)
    

class Turnosprofesional (models.Model):
    profesional = models.ForeignKey (Profesional_salud, on_delete =models.CASCADE )
    turnos_designados = models.ManyToManyField (Turnos)

#AGREGAR he datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value. En fecha.