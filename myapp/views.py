from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse('projects')

def task(request):
    return HttpResponse('tasks')
