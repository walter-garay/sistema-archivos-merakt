from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 150)
    password =  models.CharField(max_length = 30)

class Archivo(models.Model):
    archivo = models.FileField(upload_to='files/')
    fecha = models.DateField(auto_now_add=True)
    propietario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.propietario}'