from django.shortcuts import render
from .forms import PacienteForm, ProfesionalForm
from .models import paciente
# Create your views here.
def Inicio (req):
    return render (req, ("inicio.html"))

def formulariopaciente (req):
    print ("method", req.method)
    print ("POST", req.POST)
    
    if req.method == "POST":
        F_paciente = PacienteForm (req.POST)
        if F_paciente.is_valid ():
            data = F_paciente.cleaned_data
            info_paciente = paciente (
                nombre=data["nombre"], 
                apellido=data["apellido"], 
                DNI =data["DNI"], 
                fecha_de_nacimiento =data["fecha_de_nacimiento"], 
                email=data["email"],
                direccion=data["direccion"],
                Nro_telefono=data["Nro_telefono"],
                ocupacion=data["ocupacion"],
                )
            info_paciente.save ()
            return render (req, "inicio.html")
    else:
        F_paciente = PacienteForm ()
        return render(req, "formulariopaciente.html", {"Formulario_paciente": F_paciente})