from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField(max_length=30)
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad} {self.email}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'

class Articulo(models.Model):
    tipo_articulo = models.CharField(max_length=20)
    stock = models.IntegerField()
    def __str__(self):
        return f'{self.tipo_articulo} - {self.stock}'