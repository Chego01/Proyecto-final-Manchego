from django.urls import path
from AppCoderhouse.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cliente_formulario/', cliente_formulario, name="ClienteFormulario"),
    path('lista-clientes/', listar_clientes, name="ListaClientes"),

    path('empleados-formulario/', empleado_formulario, name="EmpleadosFormulario"),
    path('empleados/', listar_empleados, name = "Empleados"),
   
    path('articulo-formulario/', articulo_formulario, name="ArticuloFormulario"),
    path('lista_articulos/', listar_articulos, name='ListaArticulos'),
    path('buscar-articulos/', busqueda_articulo, name='BuscarArticulos'),
    path('buscar/', buscar, name='Buscar'),
]