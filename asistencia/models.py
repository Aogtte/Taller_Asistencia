from django.db import models

# Create your models here.
class Asistencia(models.Model):   
    nombres = models.CharField(max_length = 25)
    apellidos = models.CharField(max_length = 30)
    tipo_documento = models.CharField(max_length = 4)
    numero_documento = models.IntegerField()
    whatsapp = models.IntegerField()
    fecha = models.DateField()
    asistio =  models.BooleanField()