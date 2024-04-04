from django.urls import path
#Se importa las vistas
from myapp import views
#Como estoy en la misma carpeta, entonces uso .
from . import views

urlpatterns = [
    #Se llama a cada función que se quiere ejecutar
    path('', views.hello),
    path('about/', views.about)
]