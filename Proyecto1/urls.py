"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Blog import views
from Blog.views import detalle_pagina

urlpatterns = [
    path('', include('AppCoder.urls')),
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path ('bienvenida/', views.bienvenida, name='bienvenida'),
    path('pagina/<int:pk>/', detalle_pagina, name='detalle_pagina'),
    path('crear_blog/', views.crear_blog, name='crear_blog'),
    path('editar_entradas/', views.editar_entradas, name='editar_entradas'),
    path('editar_entrada/<int:pk>/', views.editar_entrada, name='editar_entrada'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)