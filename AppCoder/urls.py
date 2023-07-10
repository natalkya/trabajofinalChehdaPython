from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio/', inicio, name="inicio"),
    path('meetups/', meetups, name="Meetups"),
    path('setmeetups/', setmeetups, name="setmeetups"),
    path('getmeetups/', getmeetups, name="getmeetups"),
    path('buscarmeetups/', buscarmeetups, name="buscarmeetupsr"),
    path('eliminarmeetups/<titulo_meetups>', eliminarmeetups, name="eliminarmeetups"),
    path('editarmeetups/<titulo_meetups>', editarmeetups, name="editarmeetups"),
    path ('login/', loginWeb, name="login"),
    path ('registro/', registro, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = 'AppCoder/login.html'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),
    path('AboutUs/', AboutUs, name="AboutUs"),
    path('enviar_mensaje/<int:receptor_id>/', enviar_mensaje, name='enviar_mensaje'),
    path('inbox/', inbox, name='inbox'),
]