from django import forms

#Aquí se crea un forms en django
class CreateNewTask(forms.Form):
  title = forms.CharField(label="Título de tarea", max_length=200)
  description=forms.CharField(widget=forms.Textarea)

class CreateNewProject(forms.Form):
  name = forms.CharField(label="Nombre del proyecto", max_length=200)