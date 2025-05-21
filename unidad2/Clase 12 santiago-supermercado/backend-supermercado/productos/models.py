from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    id_cliente = models.IntegerField()


    def __str__(self):
        return self.nombre

