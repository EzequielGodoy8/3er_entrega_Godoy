from django.shortcuts import render

# Create your views here.
def Inicio (req):
    return render (req, ("inicio.html"))

def formulariopaciente (req):
    print