from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=30)
    numero = models.PositiveSmallIntegerField()
    departamento = models.CharField(max_length=30)
    localidad = models.CharField(max_length=30)


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    Domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)
    cuit = models.PositiveSmallIntegerField()
    telefono =models.PositiveSmallIntegerField()
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    
class Vendedor(Empleado):
    pass

class Gerente(Empleado):
    pass
    
class Administrativo(Empleado):
    pass