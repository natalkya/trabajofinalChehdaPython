from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Meetups(models.Model):
    titulo = models.CharField(max_length=100, default='')
    contenido = models.CharField(max_length=100, default='')
    fecha_publicacion = models.DateField(default=date.today)
    def __str__(self):
        return f"Titulo: {self.titulo} - Contenido: {self.contenido} - Fecha: {self.fecha_publicacion}"
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='avatares', null = True, blank = True)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username


