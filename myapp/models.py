from django.db import models

# Create your models here.
class Producto (models.Model):
    nombre = models.CharField(max_length = 200)
    precio = models.IntegerField()

class factura (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)

class cliente (models.Model):
    nombre = models.CharField(max_length=20)
    sueldo = models.FloatField()
    edad = models.IntegerField(default=0)
    hijo = models.IntegerField(null=True)