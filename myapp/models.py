from django.db import models

# Create your models here.
# En estos modelos se crean las tablas que estarán en la base de datos, entonces por ejemplo aquí se está
# creando una tabla Project
class Project(models.Model):
  # Forma de decirle a Python que esto será un texto
  name = models.CharField(max_length=200)

  #Método especial que me permite mostrar algo en la interfaz
  def __str__(self):
    return self.name


# Se crea otra tabla para las tareas
class Task(models.Model):
  title = models.CharField(max_length=200)
  # TextField es para textos más extensos que CharField
  description = models.TextField()
  # Como necesitamos relacionar los proyectos con las tareas, usamos una llave foránea para conectar ambas tablas.
  #on_delete se usa para darle la instrucción al programa de qué hacer cuando se elimine un proyecto, en este caso
  #se le está indicando que todo lo relacionado a el proyecto eliminado se eliminará en cascada.
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
