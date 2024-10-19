from django.db import models

from productos.models import Producto


# Create your models here.
# class Carrito(models.Model):
#     producto = models.ManyToManyField(Producto, through='CarritoProducto', related_name='carrito')
    

class Comprobante(models.Model):
    TIPO_VENTA = [
        ('contado', 'Contado'),
        ('credito', 'Credito')        
    ]
    
    FORMA_DE_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia')
    ]
    
    TIPO_COMPROBANTE = [
        ('factura', 'Factura'),
        ('ticket', 'Ticket')
    ]
    fecha_de_venta = models.DateField()
    tipo_de_venta = models.CharField(max_length=15, choices=TIPO_VENTA, verbose_name="Tipo de venta")
    forma_de_pago = models.CharField(max_length=15, choices=FORMA_DE_PAGO, verbose_name="Forma de pago")
    # items = models.ForeignKey(CarritoProducto, on_delete=models.CASCADE, related_name='comprobantes')
    observacion = models.TextField()

class CarritoProducto(models.Model):
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=4, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)




class Cliente_Mayorista(models.Model):
    razon_social = models.CharField(max_length=30)
    cuit = models.PositiveSmallIntegerField()
    telefono = models.PositiveSmallIntegerField()