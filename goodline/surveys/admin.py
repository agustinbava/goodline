from django.contrib import admin
from .models import Pregunta, User, Encuesta, Respuesta

admin.site.register(Pregunta)
admin.site.register(User)
admin.site.register(Encuesta)
admin.site.register(Respuesta)