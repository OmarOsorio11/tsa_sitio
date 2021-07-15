from typing import Reversible
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, EmailField
 
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=1000)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    supercategoria=models.ForeignKey('Categoria', on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    marca=models.CharField(max_length=200)
    modelo=models.CharField(max_length=200)
    capacidad=models.CharField(max_length=200)
    precio=models.IntegerField()
    moneda=models.ForeignKey('Moneda',on_delete=CASCADE)
    caracteristicas=models.TextField()
    url_img=models.CharField(max_length=100)
    url_catalogo=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    nombre_cliente=models.CharField(max_length=100)
    direccion_cliente=models.TextField()
    telefono_cliente=models.CharField(max_length=10)
    producto=models.TextField()
    cantidad=models.IntegerField()

class Moneda(models.Model):
    nombre=models.TextField()
    def __str__(self) -> str:
        return self.nombre