from django.db import models

class Asistencia(models.Model):   
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=4)
    numero_documento = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField()