from django.db import models

# Create your models here.
# class Carrito(models.Model):
    # producto = models.ManyToManyField(Producto, through='CarritoProducto', related_name='carrito')
    


class Item(models.Model):
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=4, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    
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
    items = models.ManyToManyField(Item)
    observacion = models.TextField()
    

class Cliente_Mayorista(models.Model):
    razon_social = models.CharField(max_length=30)
    cuit = models.PositiveSmallIntegerField()
    telefono = models.PositiveSmallIntegerField()