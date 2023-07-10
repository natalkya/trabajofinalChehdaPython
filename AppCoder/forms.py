from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from datetime import date
from .models import Mensaje
from django.contrib.auth.forms import UserCreationForm

class formSetMeetups (forms.Form):
    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)
    fecha_publicacion = forms.DateField(initial=date.today, widget=forms.HiddenInput)

#edicion perfil
class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description"}), required=False)
    link = forms.URLField(widget=forms.URLInput(attrs={"placeholder": "Link"}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

#edicion password
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Old password"}))
    new_password1 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"New password"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

#edicion avatar
class AvatarForm(forms.Form):
    avatar = forms.ImageField()

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']