from django.contrib import admin

# Register your models here.
from .models import Perfil, Modulo, Leccion, Sena, Ejercicio

admin.site.register(Perfil)
admin.site.register(Modulo)
admin.site.register(Leccion)
admin.site.register(Sena)
admin.site.register(Ejercicio)