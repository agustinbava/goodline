from django.shortcuts import render
from .models import Pregunta, UserForm

def home(request):
  preguntas = Pregunta.objects.filter(activa=True)
  context = {'preguntas': preguntas}
  return render(request, 'index.html', context)