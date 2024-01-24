from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ArchivoForm
from . import serializers, models
from rest_framework import viewsets
from .models import Usuario, Archivo
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = models.Archivo.objects.all()
    serializer_class = serializers.ArchivoSerializer
    
# Create your views here.

def paginaIndex(request):
    return render(request, 'index.html')

def subir(request):
    if request.method == 'POST':
        propietario = request.POST['propietario']
        archivo = request.FILES.get('archivo')
        fecha = request.POST['fecha']
        Archivo(propietario=propietario,archivo=archivo,fecha=fecha).save()
        return HttpResponse('Archivo subido exitosamente')
    else:
        return render(request, 'subir.html')

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['Nombre']
        Email = request.POST['Correo']
        password = request.POST['Password']
        Usuario(nombre=nombre, Email=Email, password=password).save()
        return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')
    
def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleUsuario = Usuario.objects.get(Email=request.POST['Correo'], password=request.POST['password'])
            print("Usuario", detalleUsuario)
            request.session['Email'] = detalleUsuario.Email
            return render(request, 'index.html')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'El nombre o password no es correcto..')

    return render(request, 'login.html')

def cerrarSesion(request):
    try:
        del request.session['Email']
    except:
        return render(request, 'principal.html')
    return render(request, 'principal.html')
