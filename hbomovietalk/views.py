from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from .forms import RegistroForm
from django.urls import reverse
from .models import Consulta
from .forms import ConsultaForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
def iniciomt(request):
    return render(request, 'iniciohbomt.html')

def iniciarsesionmt(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            try:
                usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
                return redirect('consulta')
            except Usuario.DoesNotExist:
                return redirect(reverse('registromt'))  # Redirección a URL absoluta
    else:
        form = UsuarioForm()
    return render(request, 'hbomtis.html', {'form': form})


def registromt(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('iniciarsesionmt')  # Redirige a la página de inicio de sesión después de registrarse
    else:
        form = RegistroForm()
    return render(request, 'hbomtr.html', {'form': form})

def consulta(request):
    if request.method == 'POST':
        # Recibir datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        # Guardar la consulta en la base de datos
        consulta = Consulta.objects.create(titulo=titulo, descripcion=descripcion)

        # Redirigir a la página de consultas con la nueva consulta guardada
        return redirect('consulta')
    
    # Obtener todas las consultas
    consultas = Consulta.objects.all()
    
    return render(request, 'consulta.html', {'consultas': consultas})

def chat(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)
    return render(request, 'chat.html', {'consulta': consulta})

