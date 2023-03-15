from django.forms import ModelForm
from .models import Pregunta, User, Respuesta

class RespuestasForm(ModelForm):
    class Meta:
        model = Respuesta
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nombre', 'edad', 'email']