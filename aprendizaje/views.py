from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import Perfil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Modulo
from .forms import ModuloForm
from .models import Leccion
from .forms import LeccionForm
from .models import Sena, Ejercicio
from .forms import SenaForm, EjercicioForm


def registro(request):

    if request.method == 'POST':

        formulario = RegistroUsuarioForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()

            Perfil.objects.create(
                user=usuario,
                telefono=formulario.cleaned_data['telefono'],
                rol=formulario.cleaned_data['rol']
            )
            return redirect('registro')

    else:
        formulario = RegistroUsuarioForm()

    return render(
        request,
        'aprendizaje/registro.html',
        {'formulario': formulario}
    )


def inicio(request):
    return render(request, 'aprendizaje/inicio.html')

@login_required
def inicio_usuario(request):
    return render(request, 'aprendizaje/inicio_usuario.html')

def iniciar_sesion(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio_usuario')

        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'aprendizaje/login.html')



def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')



@login_required
def lista_modulos(request):
    modulos = Modulo.objects.all()

    return render(
        request,
        'aprendizaje/modulos/lista.html',
        {'modulos': modulos}
    )



@login_required
def crear_modulo(request):

    if request.method == 'POST':
        formulario = ModuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_modulos')

    else:
        formulario = ModuloForm()

    return render(
        request,
        'aprendizaje/modulos/formulario.html',
        {'formulario': formulario}
    )



@login_required
def editar_modulo(request, id):

    modulo = Modulo.objects.get(id=id)

    if request.method == 'POST':
        formulario = ModuloForm(request.POST, instance=modulo)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_modulos')

    else:
        formulario = ModuloForm(instance=modulo)

    return render(
        request,
        'aprendizaje/modulos/formulario.html',
        {
            'formulario': formulario
        }
    )



@login_required
def eliminar_modulo(request, id):

    modulo = Modulo.objects.get(id=id)
    modulo.delete()
    return redirect('lista_modulos')



@login_required
def lista_lecciones(request):
    lecciones = Leccion.objects.all()

    return render(
        request,
        'aprendizaje/lecciones/lista.html',
        {'lecciones': lecciones}
    )



@login_required
def crear_leccion(request):

    if request.method == 'POST':
        formulario = LeccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_lecciones')

    else:
        formulario = LeccionForm()

    return render(
        request,
        'aprendizaje/lecciones/formulario.html',
        {'formulario': formulario}
    )



@login_required
def editar_leccion(request, id):

    leccion = Leccion.objects.get(id=id)
    if request.method == 'POST':

        formulario = LeccionForm(
            request.POST,
            instance=leccion
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_lecciones')

    else:
        formulario = LeccionForm(instance=leccion)

    return render(
        request,
        'aprendizaje/lecciones/formulario.html',
        {'formulario': formulario}
    )



@login_required
def eliminar_leccion(request, id):

    leccion = Leccion.objects.get(id=id)
    leccion.delete()
    return redirect('lista_lecciones')

@login_required
def crear_sena(request):

    if request.method == 'POST':
        formulario = SenaForm(
            request.POST,
            request.FILES
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_senas')

    else:
        formulario = SenaForm()

    return render(
        request,
        'aprendizaje/senas/formulario.html',
        {'formulario': formulario}
    )
@login_required
def lista_senas(request):

    senas = Sena.objects.all()
    return render(
        request,
        'aprendizaje/senas/lista.html',
        {'senas': senas}
    )

@login_required
def editar_sena(request, id):

    sena = Sena.objects.get(id=id)

    if request.method == 'POST':

        formulario = SenaForm(
            request.POST,
            request.FILES,
            instance=sena
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_senas')

    else:

        formulario = SenaForm(instance=sena)

    return render(
        request,
        'aprendizaje/senas/formulario.html',
        {'formulario': formulario}
    )

@login_required
def eliminar_sena(request, id):

    sena = Sena.objects.get(id=id)

    sena.delete()

    return redirect('lista_senas')

@login_required
def lista_ejercicios(request):

    ejercicios = Ejercicio.objects.all()

    return render(
        request,
        'aprendizaje/ejercicios/lista.html',
        {'ejercicios': ejercicios}
    )

@login_required
def crear_ejercicio(request):

    if request.method == 'POST':

        formulario = EjercicioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_ejercicios')

    else:

        formulario = EjercicioForm()

    return render(
        request,
        'aprendizaje/ejercicios/formulario.html',
        {'formulario': formulario}
    )

@login_required
def editar_ejercicio(request, id):

    ejercicio = Ejercicio.objects.get(id=id)

    if request.method == 'POST':

        formulario = EjercicioForm(
            request.POST,
            instance=ejercicio
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_ejercicios')

    else:

        formulario = EjercicioForm(instance=ejercicio)

    return render(
        request,
        'aprendizaje/ejercicios/formulario.html',
        {'formulario': formulario}
    )

@login_required
def eliminar_ejercicio(request, id):

    ejercicio = Ejercicio.objects.get(id=id)

    ejercicio.delete()

    return redirect('lista_ejercicios')