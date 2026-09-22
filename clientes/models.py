from django.db import models

# Create your models here.
from config.base_models import ModeloBase


class Cliente(ModeloBase):

    nombre = models.CharField(
        max_length=100
    )

    correo = models.EmailField(
        unique=True
    )

    telefono = models.CharField(
        max_length=20
    )

    edad = models.IntegerField()

    activo = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.nombre



class Direccion(ModeloBase):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    calle = models.CharField(
        max_length=150
    )

    ciudad = models.CharField(
        max_length=80
    )

    codigo_postal = models.IntegerField()


    def __str__(self):
        return self.calle



class Contacto(ModeloBase):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    nombre_contacto = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=50
    )

    fecha_contacto = models.DateField()


    def __str__(self):
        return self.nombre_contacto