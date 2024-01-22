from rest_framework import serializers
from .import models
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Archivo
        fields = '__all__'
