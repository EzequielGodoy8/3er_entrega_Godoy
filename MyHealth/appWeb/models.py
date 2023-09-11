from django.db import models
from django import forms
from django.utils import timezone
# Create your models here.

class paciente (models.Model):
    nombre = models.CharField (max_length=50, verbose_name="Nombre")
    apellido = models.CharField (max_length=50, verbose_name="Apellido")
    DNI = models.IntegerField(verbose_name="DNI")
    fecha_de_nacimiento = models.DateField( default= timezone.now, verbose_name="Fecha de nacimiento")
    email = models.EmailField (null=True, blank=True, verbose_name="Direccion de correo electronico")
    direccion = models.CharField (max_length=150, verbose_name="Domicilio")
    Nro_telefono = models.IntegerField (verbose_name="Numero de telefono")
    ocupacion = models.CharField (max_length=50, verbose_name="Ocupacion/profesion")
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.DNI}'
    
class Profesionalsalud (models.Model):
    nombre = models.CharField (max_length=50,verbose_name="Nombre" )
    apellido = models.CharField (max_length=50, verbose_name="Apellido")
    DNI = models.IntegerField(verbose_name="DNI")
    email = models.EmailField (max_length=50, verbose_name="Direccion de correo electronico")
    Nro_telefono = models.IntegerField(null=True, blank=True, verbose_name="Numero de telefono")
    nro_matricula = models.IntegerField (verbose_name="Numero de matricula")
    especialidad = models.CharField(max_length=50, verbose_name="especialidad")
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.especialidad}'
    
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
    horario = models.CharField (max_length=5, default= timezone.now, choices= HORARIOS_CHOICES)
    fecha = models.CharField (max_length=10, default= timezone.now, choices= FECHA_CHOICES)
    paciente = models.ForeignKey (paciente, on_delete =models.CASCADE)
    profesional = models.ForeignKey (Profesionalsalud, on_delete =models.CASCADE)

    def __str__(self):
        return f'{self.fecha} {self.horario} {self.profesional}, paciente: {self.paciente}'
    
class Turnospaciente (models.Model):
    paciente = models.ForeignKey (paciente, on_delete =models.CASCADE )
    turnos_Adquiridos = models.ManyToManyField (Turnos)
    
    def __str__(self):
        return f'Turnos adquiridos por {self.paciente}: {self.turnos_Adquiridos}'
    
class Turnosprofesional (models.Model):
    profesional = models.ForeignKey (Profesionalsalud, default= "a designar", on_delete =models.CASCADE )
    turnos_designados = models.ManyToManyField (Turnos)

    def __str__(self):
        return f'Turnos designados hacia {self.profesional}: {self.turnos_designados}'
    
