from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Usuario
from .forms import UsuarioForm
from .forms import RegistroForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def iniciarsesion(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            try:
                usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
                return redirect('home')
            except Usuario.DoesNotExist:
                return redirect(reverse('registro'))  # Redirección a URL absoluta
    else:
        form = UsuarioForm()
    return render(request, 'iniciarsesion.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('iniciarsesion')  # Redirige a la página de inicio de sesión después de registrarse
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iralhome(request):
    return render(request, 'hbo_home.html')

