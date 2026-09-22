from django.db import models
from config.base_models import ModeloBase

from productos.models import Producto


class Bodega(ModeloBase):

    nombre = models.CharField(
        max_length=100
    )

    direccion = models.CharField(
        max_length=150
    )

    capacidad = models.IntegerField()

    activa = models.BooleanField(
        default=True
    )

    fecha_registro = models.DateField()


    def __str__(self):
        return self.nombre



class MovimientoInventario(ModeloBase):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    tipo = models.CharField(
        max_length=50
    )

    cantidad = models.IntegerField()

    costo_unitario = models.FloatField()

    descripcion = models.TextField()

    fecha_movimiento = models.DateTimeField()


    def __str__(self):
        return self.tipo


#relaciona el inventario con las bodegas
class InventarioProducto(ModeloBase):

    bodega = models.ForeignKey(
        Bodega,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    stock_actual = models.IntegerField()

    stock_minimo = models.IntegerField()

    ultima_actualizacion = models.DateTimeField()

    disponible = models.BooleanField(
        default=True
    )


    def __str__(self):
        return str(self.stock_actual)