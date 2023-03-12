from django.shortcuts import render
from .models import Pregunta, UserForm

def home(request):
  # preguntas = Pregunta.objects.filter(activa=True)
  
  return render(request, 'index.html', {})