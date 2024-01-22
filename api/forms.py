from django import forms
from .models import Archivo

class ArchivoForm(forms.Form):
    class Meta:
        model = Archivo
        fields = ['propietario', 'archivo']
    