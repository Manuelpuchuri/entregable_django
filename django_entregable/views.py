from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Familiar

def nuevo_familiar(request, nombre, apellido):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_de_creacion=datetime.now())
    familiar.save()
    
    template = loader.get_template('nuevo_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado)

def ver_familiar(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiar.html')
    template_renderizado = template.render({'familiares': familiares})
    
    return HttpResponse(template_renderizado)