from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Articulo, Cliente, Empleado
from .forms import articuloformulario, clienteformulario, empleadoformulario
# Create your views here.
def inicio(req):
    return render(req,"AppCoderhouse/inicio.html")

def articulo_formulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
        formulario = articuloformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo = Articulo(tipo_articulo=data["tipo_articulo"], stock=data["stock"])
            articulo.save()
            return render(request, "AppCoderhouse/inicio.html")
    else:
        formulario = articuloformulario()
        return render(request, "AppCoderhouse/articulo_formulario.html", {"miFormulario": formulario})

def listar_articulos(req):
    lista = Articulo.objects.all()
    return render(req, "AppCoderhouse/lista_articulos.html",{"Catalogo": lista})

def cliente_formulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
        formulario_clientes = clienteformulario(request.POST)

        if formulario_clientes.is_valid():
            info = formulario_clientes.cleaned_data
            clientes = Cliente(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            clientes.save()
            return render(request, "AppCoderhouse/inicio.html")
            
    else:
        formulario_clientes = clienteformulario()
        return render(request, "AppCoderhouse/cliente_formulario.html", {"formulario": formulario_clientes})


def listar_clientes(req):
    lista_cliente = Cliente.objects.all()
    return render(req, "AppCoderhouse/lista_clientes.html",{"listado": lista_cliente})

def empleado_formulario(request):
    print('method', request.method)
    print('POST', request.POST)

    if request.method == 'POST':
        formulario_empleados = empleadoformulario(request.POST)

        if formulario_empleados.is_valid():
            dato = formulario_empleados.cleaned_data
            empleados = Empleado(nombre=dato["nombre"], apellido=dato["apellido"], edad=dato["edad"], email=dato["email"])
            empleados.save()
            return render(request, "AppCoderhouse/inicio.html")
            
    else:
        formulario_empleados = empleadoformulario()
        return render(request, "AppCoderhouse/empleados_formulario.html", {"formulario2": formulario_empleados})


def listar_empleados(req):
    lista_empleados = Empleado.objects.all()
    return render(req, "AppCoderhouse/empleados.html",{"registro": lista_empleados})


def buscar(request):
    tipo_articulo = request.GET.get("tipo_articulo", None)
    
    if tipo_articulo is not None:
        articulos = Articulo.objects.filter(tipo_articulo=tipo_articulo)
        
        if articulos.exists():
            return render(request, "AppCoderhouse/resultados.html", {"articulos": articulos})
        else:
            return HttpResponse("No se encontraron resultados para la búsqueda.")
    else:
        return HttpResponse("Debe agregar un tipo de artículo en la consulta.")


def busqueda_articulo(request):
    return render(request, "AppCoderhouse/buscar_articulos.html")