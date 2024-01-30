from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from .forms import ArchivoForm
from . import serializers, models
from rest_framework import viewsets
from .models import Usuario, Archivo
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.http import FileResponse
import os





class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = models.Archivo.objects.all()
    serializer_class = serializers.ArchivoSerializer
    
# Create your views here.

def descargar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivo, pk=archivo_id)
    response = FileResponse(archivo.archivo, as_attachment=True)
    return response

def eliminar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivo, pk=archivo_id)
    ruta_archivo = archivo.archivo.path
    archivo.delete()
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
    return redirect('subir')   

def subir_archivo(request):
    if request.method == 'POST':
        formulario = ArchivoForm(request.POST, request.FILES)
        print("AQUI1")
        user_id = request.session.get('user_id')
        if formulario.is_valid():
            archivo_instance = formulario.save(commit=False)
            archivo_instance.propietario = Usuario.objects.get(id=user_id)

            archivo_instance.save()
            
            print("AQUI2")
            return redirect('subir')
    else:
        print("AQUI3")
        formulario = ArchivoForm()

    return render(request, 'subir.html', {'formulario': formulario})

def paginaIndex(request):
    return render(request, 'index.html')

def obtenerArchivos(request):
    archivos = Archivo.objects.all()
    if request.method == 'GET':
        return render(request, 'subir.html', {'archivos': archivos})

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['Nombre']
        apellidos = request.POST['Apellidos']
        Email = request.POST['Correo']
        password = request.POST['Password']
        Usuario(nombre=nombre, apellidos=apellidos, Email=Email, password=password).save()
        return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')
    
def paginaLogin(request):
    if request.method == 'POST':
        try:
            detalleUsuario = Usuario.objects.get(Email=request.POST['Correo'], password=request.POST['password'])
            print("Usuario", detalleUsuario)
            request.session['user_email'] = detalleUsuario.Email
            request.session['user_id'] = detalleUsuario.pk
            request.session['user_name'] = detalleUsuario.nombre
            request.session['user_apellido'] = detalleUsuario.apellidos


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