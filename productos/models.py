from django.db import models

# Create your models here.
from config.base_models import ModeloBase

class Categoria(ModeloBase):

    nombre = models.CharField(
        max_length=100
    )

    descripcion = models.TextField()

    activa = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.nombre

class Marca(ModeloBase):

    nombre = models.CharField(
        max_length=100
    )

    pais_origen = models.CharField(
        max_length=80
    )

    fundacion = models.DateField()


    def __str__(self):
        return self.nombre

class Producto(ModeloBase):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        max_length=100
    )

    descripcion_corta = models.CharField(
        max_length=200,
        default=""
    )

    precio = models.FloatField()

    cantidad = models.IntegerField()

    disponible = models.BooleanField(
        default=True
    )