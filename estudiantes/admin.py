from django.contrib import admin
# 1. Primero importamos los modelos
from .models import Estudiante, Producto

# 2. Luego los registramos
admin.site.register(Estudiante)
admin.site.register(Producto)