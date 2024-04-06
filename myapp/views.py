#Render permite usar las plantillas de django para renderizar htmls

from django.shortcuts import render
#Se importa Json porque es un lenguaje fácil de entender para el navegador
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
#Esta importación permite en lugar de devolver un error, mostrar al usuario que no se ha encontrado la página con el 404
from django.shortcuts import get_object_or_404

# Create your views here.

#Nueva función que será la primera cuando se visite el servidor
def index(request):
    return HttpResponse('Index page')

#Ahora la función hello requiere dos parámetros, así que para poderla ejecutar tenemos que pasar otro string.
def hello(request, username):
    #Aquí se está concatenando el username al hello
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse("About")

def projects(request):
    #Para usar el Json primero se debe convertir los projects en una lista de python
    projects = list(Project.objects.values())
    #Al usar Json response, ya no necesitamos usar un String, sino que podemos directamente pasarle la lista de los 
    #objetos Project
    return JsonResponse(projects, safe=False)

#Ahora tasks tendrá como otro param el id
def tasks(request, id):
    #Se guarda una tarea con el id especificado
    task = get_object_or_404(Task, id=id)
    #Se usa % para concatenar el titulo de la tarea
    return HttpResponse('task: %s' % task.title)
