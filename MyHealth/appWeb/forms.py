from django.forms import ModelForm
from appWeb.models import paciente,Profesionalsalud

class PacienteForm (ModelForm):
    class Meta:
        model = paciente
        fields = ["nombre","apellido","DNI","fecha_de_nacimiento", "email", "direccion","Nro_telefono","ocupacion"]

class ProfesionalForm (ModelForm):
    class Meta:
        model = Profesionalsalud
        fields = ["nombre","apellido","DNI","email","Nro_telefono", "nro_matricula","especialidad"]
        