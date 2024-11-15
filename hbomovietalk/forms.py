from django import forms
from .models import Usuario
from .models import Consulta


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

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['titulo', 'descripcion']
