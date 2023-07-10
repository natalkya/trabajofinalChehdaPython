from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import Pagina
from .forms import PageForm
from django.contrib.auth.decorators import login_required

def bienvenida (request):
    blog = Pagina.objects.all()
    return render (request, "Proyecto1/plantillas/template1.html", {"blog":blog})

def detalle_pagina(request, pk):
    pagina = get_object_or_404(Pagina, pk=pk)
    return render(request, 'Proyecto1/plantillas/detalle_pagina.html', {'pagina': pagina})

@login_required 
def crear_blog(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.autor = request.user  
            blog.save()
            return redirect('bienvenida') 
    else:
        form = PageForm()
    
    return render(request, 'Proyecto1/plantillas/crear_blog.html', {'form': form})

@login_required 
def editar_entradas(request):
    entradas = Pagina.objects.all()
    return render(request, 'Proyecto1/plantillas/editar_entradas.html', {'entradas': entradas})

@login_required 
def editar_entrada(request, pk):
    entrada = get_object_or_404(Pagina, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('editar_entradas')
    else:
        form = PageForm(instance=entrada)
    return render(request, 'Proyecto1/plantillas/editar_entrada.html', {'form': form})