#Render permite usar las plantillas de django para renderizar htmls

from django.shortcuts import render, redirect
#Se importa Json porque es un lenguaje fácil de entender para el navegador
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
#Esta importación permite en lugar de devolver un error, mostrar al usuario que no se ha encontrado la página con el 404
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

#Nueva función que será la primera cuando se visite el servidor
def index(request):
    title = 'Django course!!'
    #Ahora se recibe como parámetro un diccionario que permitirá asignar el valor del título 
    return render(request, 'index.html', {
        'title': title
    })

#Ahora la función hello requiere dos parámetros, así que para poderla ejecutar tenemos que pasar otro string.
def hello(request, username):
    #Aquí se está concatenando el username al hello
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    #Para usar el Json primero se debe convertir los projects en una lista de python
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #Al usar Json response, ya no necesitamos usar un String, sino que podemos directamente pasarle la lista de los 
    #objetos Project
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

#Ahora tasks tendrá como otro param el id
def tasks(request):
    #Se guarda una tarea con el id especificado
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    #Se usa % para concatenar el titulo de la tarea
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

#Aquí se usa el archivo de forms.py para usar el form creado allá
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })

