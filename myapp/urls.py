from django.urls import path
#Se importa las vistas
from myapp import views
#Como estoy en la misma carpeta, entonces uso .
from . import views

urlpatterns = [
    #Se llama a cada función que se quiere ejecutar
    path('', views.index),
    path('about/', views.about),
    #Para poder ejecutar el hello, tenemos que ir a hello/nombre-del-usuario o cualquier otra cosa que sea string
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project)
]