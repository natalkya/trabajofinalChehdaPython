from django import forms
from .models import Pagina

class PageForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['title', 'subtitle', 'content', 'image', 'posted', 'order', 'autor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'}),
            'image': forms.URLInput(attrs={'class':'form-control', 'placeholder': 'URL de la imagen'}),
            'posted': forms.DateTimeInput(attrs={'class': 'datepicker'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
        }