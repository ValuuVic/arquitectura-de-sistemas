from django.db import models

# Create your models here.
from config.base_models import ModeloBase

from clientes.models import Cliente
from productos.models import Producto


class OrdenCompra(ModeloBase):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    codigo_orden = models.CharField(
        max_length=25,
        unique=True
    )

    fecha_solicitud = models.DateField()

    hora_generacion = models.TimeField()

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    prioridad = models.CharField(
        max_length=30
    )

    confirmado = models.BooleanField(
        default=False
    )


    def __str__(self):
        return self.codigo_orden



class DetalleOrden(ModeloBase):

    orden = models.ForeignKey(
        OrdenCompra,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    unidades = models.PositiveIntegerField()

    descuento_aplicado = models.FloatField(
        default=0
    )

    observacion = models.TextField(
        blank=True
    )

    requiere_revision = models.BooleanField(
        default=False
    )


    def __str__(self):
        return f"Detalle {self.id}"



class Factura(ModeloBase):

    orden = models.OneToOneField(
        OrdenCompra,
        on_delete=models.CASCADE
    )

    numero_autorizacion = models.CharField(
        max_length=60
    )

    fecha_emision = models.DateTimeField()

    metodo_pago = models.CharField(
        max_length=40
    )

    total_pagado = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    enviada_cliente = models.BooleanField(
        default=False
    )


    def __str__(self):
        return self.numero_autorizacion