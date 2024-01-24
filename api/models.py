from django.db import models
import os

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 150)
    password =  models.CharField(max_length = 30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class Archivo(models.Model):
    archivo = models.FileField(upload_to='files/')
    nombre = models.CharField(max_length = 256, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    propietario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        if not self.nombre:
            self.nombre = os.path.basename(self.archivo.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.propietario}'
    

