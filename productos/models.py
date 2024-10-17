from django.db import models

# Create your models here.
class Insumo(models.Model):
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    medida = models.CharField(max_length=30)
    punto_de_pedido = models.DecimalField(max_digits=6, decimal_places=2)
    


class Producto(models.Model):
    UNIDADES = [
        ('unidad', 'u.'),
        ('gramo', 'gr.'),
        ('kilogramo', 'kg.')
    ]
    
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES)
    descripcion = models.TextField()
    stock = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)