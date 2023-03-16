from django.shortcuts import render
from django.views import View
from .models import Pregunta 
from .forms import RespuestasForm, UserForm
from django.http import HttpResponseRedirect, HttpResponse


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
    
    if userForm.is_valid() and respuestasForm.is_valid():
      userForm.save()
      respuestasForm.save()
      return HttpResponseRedirect('/thanks/')
      
  return render(request, 'index.html', context)
  

def contactus(request):
  return render(request, 'contactus.html', {})

def thanks(request):
  return render(request, 'thanks.html', {})