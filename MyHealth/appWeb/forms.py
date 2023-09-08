from django.forms import ModelForm
from appWeb.models import *

class PacienteForm (ModelForm):
    class meta:
        model = paciente
        fields = ["nombre","apellido","DNI","fecha_de_nacimiento", "email", "direccion","Nro_telefono","ocupacion"]

class ProfesionalForm (ModelForm):
    class meta:
        model = Profesional_salud
        fields = ["nombre","apellido","DNI","fecha_de_nacimiento", "email", "nro_matricula","especialidad"]
        