from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .forms import PacienteForm, ProfesionalForm, TurnosForm
from .models import paciente, Turnospaciente, Turnosprofesional
# Create your views here.
def Inicio (req):
    return render (req, ("inicio.html"))

def Pacientes (req):
        return render (req, ("pacientes.html"))

def Profesionales (req):
        return render (req, ("profesionales.html"))

def Turnos (req):
        return render (req, ("turnos.html"))

def Consultarturnos (req):
    return render (req, ("consultarturnos.html"))

#Views para formulario tipo POST

def formulariopaciente (req):
    F_paciente = PacienteForm ()
    if req.method == "POST":
        F_paciente = PacienteForm (data=req.POST)
        if F_paciente.is_valid ():
            F_paciente.save ()
            return redirect (reverse('Formulariopaciente')+'?ok',)
        else:
            return redirect (reverse('Formulariopaciente')+'?error',)

    return render(req, "formulariopaciente.html", {"formulariopaciente": F_paciente})

def formularioprofesional (req):
    F_profesional = ProfesionalForm ()
    if req.method == "POST":
        F_profesional = ProfesionalForm (data=req.POST)
        if F_profesional.is_valid ():
            F_profesional.save()
            return redirect (reverse('Formularioprofesional')+'?ok',)
        else:
            return redirect (reverse('Formularioprofesional')+'?error',)

    return render(req, "formularioprofesional.html", {"formularioprofesional": F_profesional})

def formularioadquirirturnos(req):
    F_turnos = TurnosForm()

    if req.method == "POST":
        F_turnos = TurnosForm(data=req.POST)
        if F_turnos.is_valid():
            # Crea una instancia de Turnos pero asegúrate de establecer el paciente adecuado
            nuevo_turno = F_turnos.save(commit=False)  # No lo guardes en la base de datos todavía
            # Obtén el paciente relacionado (por ejemplo, por su ID)
            Paciente_id = req.POST['paciente']  # Asegúrate de que 'paciente' corresponda al campo en tu formulario
            Paciente = paciente.objects.get(id=Paciente_id)
            nuevo_turno.Paciente = Paciente  # Establece el paciente en el nuevo_turno
            nuevo_turno.save()  # Ahora guárdalo en la base de datos

            return redirect(reverse('Formularioadquirirturnos') + '?ok',)
        else:
            return redirect(reverse('Formularioadquirirturnos') + '?error',)

    return render(req, "formularioadquirirturnos.html", {"adquirirturno": F_turnos})

#Views para formulario tipo GET
def busquedapacientes (req):
    return render (req,"busquedapacientes.html")
def buscarpacientes(req: HttpRequest):
    try:
        if req.GET ["nombre"]:
            nombre = req.GET ["nombre"]
            Paciente = paciente.objects.filter(nombre=nombre)
            return render(req, "resultadobusquedapacientes.html", {"busquedapaciente": Paciente})
    except:
        return HttpResponse (f"ocurrio un error, vuelva a ingresar a la pagina")
