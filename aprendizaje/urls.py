from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio_usuario, name='inicio_usuario'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('modulos/', views.lista_modulos, name='lista_modulos'),
    path('modulos/crear/', views.crear_modulo, name='crear_modulo'),
    path('modulos/editar/<int:id>/', views.editar_modulo, name='editar_modulo'),
    path('modulos/eliminar/<int:id>/', views.eliminar_modulo, name='eliminar_modulo'),
    path('lecciones/', views.lista_lecciones, name='lista_lecciones'),
    path('lecciones/crear/', views.crear_leccion, name='crear_leccion'),
    path('lecciones/editar/<int:id>/', views.editar_leccion, name='editar_leccion'),
    path('lecciones/eliminar/<int:id>/', views.eliminar_leccion, name='eliminar_leccion'),
    path('senas/', views.lista_senas, name='lista_senas'),
    path('senas/crear/', views.crear_sena, name='crear_sena'),
    path('senas/editar/<int:id>/', views.editar_sena, name='editar_sena'),
    path('senas/eliminar/<int:id>/', views.eliminar_sena, name='eliminar_sena'),
    path('ejercicios/', views.lista_ejercicios, name='lista_ejercicios'),
    path('ejercicios/crear/', views.crear_ejercicio, name='crear_ejercicio'),
    path('ejercicios/editar/<int:id>/', views.editar_ejercicio, name='editar_ejercicio'),
    path('ejercicios/eliminar/<int:id>/', views.eliminar_ejercicio, name='eliminar_ejercicio'),
]
