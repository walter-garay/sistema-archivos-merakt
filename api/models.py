from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 150)
    password =  models.CharField(max_length = 30)

class Archivo(models.Model):
    archivo = models.FileField(upload_to='api/')
    fecha = models.DateField(max_length=10,null=False,blank=False)
    propietario = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.propietario}'