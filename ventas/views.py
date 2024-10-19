from django.shortcuts import render

from ventas.models import Comprobante

# Create your views here.
def nueva_venta(request):
    return render(request, 'ventas/venta.html')

def pagar(request):
    return render(request, 'ventas/genrerar_comprobante.html')

def listar_ventas(request):
    comprobantes = Comprobante.object.all()
    return render(request, 'ventas/lista_ventas.html', {'comprobantes': comprobantes})