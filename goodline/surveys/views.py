from django.shortcuts import render
from django.views import View
from .models import Pregunta 
from .forms import RespuestasForm, UserForm


def home(request):
  userForm = UserForm()
  preguntas = Pregunta.objects.filter(activa=True)
  respuestasForm = RespuestasForm()
  
  context = {
    'userForm': userForm,
    'preguntas': preguntas,
    'respuestasForm': respuestasForm
  }
  
  if request.method == 'POST':
    userForm = UserForm(request.POST)
    respuestasForm = RespuestasForm(request.POST)
    
    if userForm.is_valid():
      userForm.save()
      
    if respuestasForm.is_valid():
      respuestasForm.save()
      
  return render(request, 'index.html', context)
  

def contactus(request):
  return render(request, 'contactus.html', {})