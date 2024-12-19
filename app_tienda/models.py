from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Zapatillas(models.Model):
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    modelo = models.CharField(max_length=30)
    precio = models.FloatField()
    talle_arg = models.IntegerField()
    vendedor = models.CharField(max_length=30)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f"Modelo: {self.modelo} - Precio: {self.precio} - Vendedor: {self.vendedor}"

class Botines(models.Model):
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    modelo = models.CharField(max_length=30)
    precio = models.FloatField()
    talle_arg = models.IntegerField()
    vendedor = models.CharField(max_length=30)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f"Modelo: {self.modelo} - Precio: {self.precio} - Vendedor: {self.vendedor}"

class Ropa(models.Model):
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    modelo = models.CharField(max_length=30)
    precio = models.FloatField()
    talle_arg = models.CharField(max_length=5)
    vendedor = models.CharField(max_length=30)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f"Modelo: {self.modelo} - Precio: {self.precio} - Vendedor: {self.vendedor}"

class Otros_Productos(models.Model):
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    producto = models.CharField(max_length=30)
    precio = models.FloatField()
    vendedor = models.CharField(max_length=30)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f"Producto: {self.producto} - Precio: {self.precio} - Vendedor: {self.vendedor}"

class Vendedores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.BigIntegerField(null=True)
    def __str__(self):
        return f"Vendedor: {self.apellido}, {self.nombre} - Email: {self.email} - Teléfono: {self.telefono}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.BigIntegerField(null=True)
    def __str__(self):
        return f"Cliente: {self.apellido}, {self.nombre} - Email: {self.email} - Teléfono: {self.telefono}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.BigIntegerField()
    descripcion = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="foto_de_perfil/", null=True, blank=True)
    telefono = models.IntegerField(null=True)
    def __str__(self):
        return f"Usuario: {self.user}"