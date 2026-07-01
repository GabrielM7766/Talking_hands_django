from django.db import models
from django.contrib.auth.models import User

ROLES = (
    ('ADMIN', 'Administrador'),
    ('INST', 'Instructor o administrativo'),
    ('APRE', 'Aprendiz'),
)

class Perfil(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    rol = models.CharField(
        max_length=5,
        choices=ROLES,
        default='APRE'
    )

    telefono = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.user.username
    

class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Leccion(models.Model):
    modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    

class Sena(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre
    

class Ejercicio(models.Model):
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE
    )

    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=100)

    def __str__(self):
        return self.pregunta