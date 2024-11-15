"""
URL configuration for HBO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Plataforma import views as plataformaViews
from hbomovietalk import views as hbomtViews

urlpatterns = [
    path('', plataformaViews.inicio),
    path('iniciarsesion/', plataformaViews.iniciarsesion, name='iniciarsesion'),
    path('registro/', plataformaViews.registro, name='registro'),
    path('iralhome/', plataformaViews.iralhome, name='home'),
    path('servicio/', hbomtViews.iniciomt),
    path('iniciarsesionmt/', hbomtViews.iniciarsesionmt, name='iniciarsesionmt'),
    path('registrarsemt/', hbomtViews.registromt, name='registromt'),
    path('consulta/', hbomtViews.consulta, name='consulta'), 
    path('chat/<int:consulta_id>/', hbomtViews.chat, name='chat'),
   
]
