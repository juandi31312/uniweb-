from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Estudiante, Producto


# --- VISTAS DE ESTUDIANTES ---

def home(request):
    return render(request, "estudiantes/home.html", {"titulo": "Home estudiantes"})


def registro(request):
    error = None
    if request.method == "POST":
        nombre_formulario = request.POST.get("nombre", "").strip()
        edad_formulario = request.POST.get("edad", "").strip()

        if nombre_formulario and edad_formulario:
            try:
                edad = int(edad_formulario)
                if edad <= 0:
                    error = "La edad debe ser mayor a 0."
                else:
                    Estudiante.objects.create(nombre=nombre_formulario, edad=edad)
                    return redirect("lista_estudiantes")
            except ValueError:
                error = "La edad debe ser un número válido."
        else:
            error = "Todos los campos son obligatorios."

    return render(request, "estudiantes/registro_estudiante.html", {"error": error})


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista_estudiantes.html", {"estudiantes": estudiantes})


# --- VISTAS DE PRODUCTOS ---

def registrar_producto(request):
    error = None
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        precio = request.POST.get("precio", "").strip()

        if nombre and precio:
            try:
                precio_decimal = float(precio)
                if precio_decimal < 0:
                    error = "El precio no puede ser negativo."
                else:
                    Producto.objects.create(nombre=nombre, precio=precio_decimal)
                    return redirect("lista_productos")
            except ValueError:
                error = "El precio debe ser un número válido."
        else:
            error = "Todos los campos son obligatorios."

    return render(request, "estudiantes/registro_producto.html", {"error": error})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "estudiantes/lista_productos.html", {"productos": productos})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        precio = request.POST.get("precio", "").strip()

        if nombre and precio:
            try:
                producto.nombre = nombre
                producto.precio = float(precio)
                producto.save()
                return redirect("lista_productos")
            except ValueError:
                error = "El precio debe ser un número válido."
        else:
            error = "Todos los campos son obligatorios."

    return render(request, "estudiantes/editar_producto.html", {"producto": producto, "error": error})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect("lista_productos")
    return render(request, "estudiantes/confirmar_eliminar_producto.html", {"producto": producto})


def inicio(request):
    return HttpResponse("Hola, esta es mi app estudiantes 🔥")
