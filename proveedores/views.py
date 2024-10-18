from django.shortcuts import render

from productos.models import Insumo
from proveedores.models import Pedido, Proveedor, Recepcion

# Create your views here.
#proveedores
def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'Proveedores': proveedores})

def alta_proveedor(request):
    return render(request, 'proveedores/alta_proveedores.html')

#pedidos
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'Pedidos': pedidos})

def nuevo_pedido(request):
    return render(request, 'pedidos/nuevo_pedidos.html')

#recepciones
def listar_recepciones(request):
    recepciones = Recepcion.objects.all()
    return render(request, 'recepciones/lista_recepciones.html', {'recepcion': recepciones})

def nueva_recepcion(request):
    return render(request, 'recepciones/nueva_recepcion.html')