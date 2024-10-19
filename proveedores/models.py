from django.db import models

# Create your models here.
class Proveedor (models.Model):
    razon_social = models.CharField(max_length=30)
    cuit = models.PositiveSmallIntegerField()
    telefono = models.PositiveSmallIntegerField() 
    
    def __str__(self):
        return f"{self.razon_social}, telefono: {self.telefono}"
    

class Pedido (models.Model):
    ESTADO = [
        ('Pendiente', 'Pendiente'),
        ('Recibido', 'Recibido'),
        ('Cancelado', 'Cancelado'),
    ]
    
    cantidad = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    observacion = models.TextField()
    estado = models.CharField(
        choices= ESTADO,
        default='Pendiente',
    )
    ##insumo
    
class Recepcion (models.Model):
    fecha_recepcion = models.DateField()
    ##insumo
    cantidad_recibida = models.PositiveSmallIntegerField()
    precio_unitario = models.DecimalField(max_digits=999, decimal_places=2)
    precio_total = models.DecimalField(max_digits=9999, decimal_places=2)
    conformidad = models.TextField()
    observacion = models.TextField()
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)