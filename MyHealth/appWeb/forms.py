from django.forms import forms, ModelForm
from appWeb.models import paciente,Profesionalsalud, Turnos, Turnospaciente, Turnosprofesional


class PacienteForm(ModelForm):  
    class Meta:
        model = paciente
        fields = "__all__"

class ProfesionalForm (ModelForm):
    class Meta:
        model = Profesionalsalud
        fields = "__all__"
        
class TurnosForm (ModelForm):
    class Meta:
        model = Turnos
        fields = "__all__"