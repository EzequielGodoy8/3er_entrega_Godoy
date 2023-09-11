from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from .forms import PacienteForm, ProfesionalForm, TurnosForm
from .models import paciente
# Create your views here.
def Inicio (req):
    return render (req, ("inicio.html"))

def Pacientes (req):
        return render (req, ("pacientes.html"))

def Profesionales (req):
        return render (req, ("profesionales.html"))

def Turnos (req):
        return render (req, ("turnos.html"))




def formulariopaciente (req):
    F_paciente = PacienteForm ()
    if req.method == "POST":
        F_paciente = PacienteForm (data=req.POST)
        if F_paciente.is_valid ():
            PacienteForm.save (F_paciente)
            return redirect (reverse('formulariopaciente')+'?ok',)
        else:
            return redirect (reverse('formulariopaciente')+'?error',)

    return render(req, "formulariopaciente.html", {"formulariopaciente": F_paciente})

def formularioprofesional (req):
    F_profesional = ProfesionalForm ()
    if req.method == "POST":
        F_profesional = ProfesionalForm (data=req.POST)
        if F_profesional.is_valid ():
            ProfesionalForm.save (F_profesional)
            return redirect (reverse('Formularioprofesional')+'?ok',)
        else:
            return redirect (reverse('Formularioprofesional')+'?error',)

    return render(req, "formularioprofesional.html", {"formularioprofesional": F_profesional})

def formularioadquirirturnos (req):
    F_turnos = TurnosForm ()
    if req.method == "POST":
        F_turnos = ProfesionalForm (data=req.POST)
        if F_turnos.is_valid ():
            ProfesionalForm.save ()
            return redirect (reverse('formularioadquirirturnos')+'?ok',)
        else:
            return redirect (reverse('formularioadquirirturnos')+'?error',)

    return render(req, "formularioadquirirturnos.html", {"adquirirturno": F_turnos})

def buscarturnosadquiridos (req: HttpRequest):
    if req.GET["Turno"]:
        pass
