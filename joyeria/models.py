from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    destacada = models.BooleanField(default=False) 

    def __str__(self):
        return self.nombre


class Material(models.Model):
    nombre = models.CharField(max_length=50) 
    quilates = models.CharField(max_length=20, blank=True, null=True) 
    color = models.CharField(max_length=30, blank=True, null=True) 
    
    def __str__(self):
        return f"{self.nombre} {self.quilates} - {self.color}"


class Joya(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2) 
    stock = models.IntegerField(default=1)
    peso_gramos = models.DecimalField(max_digits=5, decimal_places=2, null=True) 
    descripcion = models.TextField(blank=True, null=True) 
    fecha_creacion = models.DateTimeField(default=timezone.now) 
    

    categoria_nombre = models.CharField(max_length=50, blank=True) 
    material_nombre = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
