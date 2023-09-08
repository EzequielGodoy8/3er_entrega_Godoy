from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def probando_templates (req):
    plantilla = loader.get_template ("template1.html") 
    documento = plantilla.render ({"my_name": "Ezequiel", "notas": [5,4,7,10,8]})
    return HttpResponse (documento)