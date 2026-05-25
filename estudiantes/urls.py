from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),

    # Rutas de Estudiantes
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/registro/', views.registro, name='registro_estudiante'),

    # Rutas de Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.registrar_producto, name='registro_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
