from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pregunta, User, Encuesta

admin.site.register(Pregunta)
admin.site.register(User)
admin.site.register(Encuesta)