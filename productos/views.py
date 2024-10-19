from django.shortcuts import render

from productos.models import Insumo, Producto

# Create your views here.
#insumos
def listar_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumos/lista_insumos.html', {'insumos': insumos})

def cargar_insumo(request):
    return render(request, 'insumos/cargar_insumo')

#productos
def listar_insumos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def cargar_producto(request):
    return render(request, 'productos/cargar_producto.html')

