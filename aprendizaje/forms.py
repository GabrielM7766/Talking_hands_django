from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil
from .models import Modulo
from .models import Leccion
from .models import Sena
from .models import Ejercicio


class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=20)
    rol = forms.ChoiceField(choices=Perfil._meta.get_field('rol').choices)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'telefono',
            'rol',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user

class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo
        fields = ['nombre', 'descripcion']

class LeccionForm(forms.ModelForm):

    class Meta:
        model = Leccion
        fields = ['modulo', 'titulo', 'descripcion']

class SenaForm(forms.ModelForm):

    class Meta:
        model = Sena
        fields = ['nombre', 'descripcion', 'leccion']

class EjercicioForm(forms.ModelForm):

    class Meta:
        model = Ejercicio
        fields = [
            'leccion',
            'pregunta',
            'respuesta'
        ]