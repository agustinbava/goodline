from django.db import models

class Encuesta(models.Model):
  titulo = models.CharField(max_length=2000)
  marca = models.CharField(max_length=100)
  surcursal = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=2000)
  mensaje_bienvenida = models.CharField(max_length=2000)
  mensaje_final = models.CharField(max_length=1000)
  estado = models.BooleanField(default=True)
  fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=False)
  fecha_expiracion = models.DateTimeField(auto_now=False, auto_now_add=False)
  fecha_actualizada = models.DateTimeField(auto_now=False, auto_now_add=False)
  
  def __str__(self):
    return self.titulo
  
  
class Pregunta(models.Model):
  encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
  nombre = models.CharField(max_length=1000)
  respuesta = models.CharField(max_length=2000)
  tipo_pregunta = models.CharField(max_length=100)
  fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=False)
  fecha_expiracion = models.DateTimeField(auto_now=False, auto_now_add=False)
  fecha_respuesta = models.DateTimeField(auto_now=False, auto_now_add=False)
  
  def __str__(self):
    return self.nombre
  
  
class User(models.Model):
  nombre = models.CharField(max_length=100)
  edad = models.IntegerField()
  respuestas = models.ManyToManyField(Pregunta)
  estadio = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nombre