from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AppCoder.models import Meetups, Avatar, Mensaje
from AppCoder.forms import *
from datetime import date
from .forms import MensajeForm
from .models import UserProfile

#vistas principales

def inicio(request):
    avatar = getavatar(request)
    return render(request, "AppCoder/inicio.html", {"avatar": avatar})

def meetups(request):
    meetups_objects = Meetups.objects.all()
    return render(request, "AppCoder/meetups.html", {"meetups": meetups_objects})

def AboutUs(request):
    return render(request, "AppCoder/AboutUs.html")

#meetups
@login_required
def setmeetups(request):
    if request.method == 'POST':
        miFormulario2 = formSetMeetups(request.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            meetups = Meetups(titulo=data["titulo"], contenido=data["contenido"], fecha_publicacion=date.today())    
            meetups.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario2 = formSetMeetups()
    return render(request, "AppCoder/setmeetups.html", {"miFormulario2": miFormulario2})

def getmeetups(request):
    return render(request, "AppCoder/getmeetups.html")

def buscarmeetups(request):
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        meetups = Meetups.objects.filter(titulo__icontains=titulo)
        return render(request, "AppCoder/getmeetups.html", {"meetups": meetups})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@login_required 
def eliminarmeetups(request, titulo_meetups):
    if request.user.is_superuser:
        try:
            meetups = Meetups.objects.get(titulo=titulo_meetups)
            meetups.delete()
            miFormulario2 = formSetMeetups()
            meetups = Meetups.objects.all()
            return render(request, "AppCoder/setmeetups.html", {"miFormulario2": miFormulario2, "meetups": meetups})
        except Meetups.DoesNotExist:
            raise Http404("meetups no existe")
    else:
        return render(request, "AppCoder/acceso_restringido.html")

@login_required 
def editarmeetups(request, titulo_meetups):
    meetups = Meetups.objects.get(titulo=titulo_meetups)

    if request.method == 'POST':
        miFormulario2 = formSetMeetups(request.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            meetups.titulo = data['titulo']
            meetups.contenido = data['contenido']
            meetups.fecha_publicacion = date.today()
            meetups.save()
            miFormulario2 = formSetMeetups()
            meetups_objects = Meetups.objects.all()
            return render(request, "AppCoder/setmeetups.html", {"miFormulario2": miFormulario2, "meetups": meetups_objects})
    else:
        miFormulario2 = formSetMeetups(initial={'titulo': meetups.titulo, 'contenido': meetups.contenido})
    return render(request, "AppCoder/editarmeetups.html", {"miFormulario2": miFormulario2})

#login
def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request,"AppCoder/inicio.html")
        else:
            return render(request, 'AppCoder/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'AppCoder/login.html')

#registro
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    
    return render(request, 'AppCoder/registro.html', {'form': form})

#perfil
@login_required  
def perfilview(request):
    return render(request, 'AppCoder/Perfil/Perfil.html')

@login_required  
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id=usuario.id)
    try:
        user_profile = UserProfile.objects.get(user=usuario)  # Obtenemos el perfil de usuario asociado
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            email = request.user.email
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            if user_profile:
                user_profile.description = form.cleaned_data.get('description')
                user_profile.link = form.cleaned_data.get('link')
                user_profile.save()
            else:
                UserProfile.objects.create(user=usuario, description=form.cleaned_data.get('description'), link=form.cleaned_data.get('link'))
            user_basic_info.save()
            return render(request, 'AppCoder/Perfil/Perfil.html', {'email': email})
    else:
        initial_data = {
            'username': usuario.username,
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name
        }
        if user_profile:
            initial_data['description'] = user_profile.description
            initial_data['link'] = user_profile.link
        form = UserEditForm(initial=initial_data)

    return render(request, 'AppCoder/Perfil/editarPerfil.html', {"form": form})


    
#password
@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las contraseñas no coinciden")
        return render(request, "AppCoder/inicio.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'AppCoder/Perfil/changePassword.html', {"form": form})

#avatar
def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "AppCoder/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "AppCoder/Perfil/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

@login_required
def enviar_mensaje(request, receptor_id):
    receptor = User.objects.get(id=receptor_id)
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.receptor_id = receptor_id
            mensaje.save()
            return redirect('inbox')  
    else:
        form = MensajeForm()
    
    return render(request, 'AppCoder/enviar_mensaje.html', {'form': form, 'receptor': receptor})

def obtener_usuarios():
    usuarios = User.objects.values_list('id', 'username')
    return usuarios

@login_required
def inbox(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user)
    usuarios = obtener_usuarios()
    return render(request, 'AppCoder/inbox.html', {'mensajes_recibidos': mensajes_recibidos, 'usuarios': usuarios})