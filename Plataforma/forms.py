from django import forms
from .models import Peliculas
from .models import Usuario

class PeliculasForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'contrasena']
        widgets = {'contrasena': forms.PasswordInput(),}

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),  # Para que el campo de contraseña sea seguro
        }
