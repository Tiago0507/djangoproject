from django.urls import path
#Se importa las vistas
from myapp import views
#Como estoy en la misma carpeta, entonces uso .
from . import views

urlpatterns = [
    #Se llama a cada función que se quiere ejecutar
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    #Para poder ejecutar el hello, tenemos que ir a hello/nombre-del-usuario o cualquier otra cosa que sea string
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project")
]