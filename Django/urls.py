"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('usuario', views.UsuarioViewSet)
router.register('archivo', views.ArchivoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='api/')),
    path('index', views.paginaIndex),
    path('subir', views.subir, name='subir'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.paginaLogin, name='paginaLogin'),
    path('principal', views.cerrarSesion, name='principal'),
    path('descargar_archivo/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
    path('eliminar_archivo/<int:archivo_id>/', views.eliminar_archivo, name='eliminar_archivo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
