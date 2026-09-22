from django.db import models
from config.base_models import ModeloBase

#datos del proveedor
class Proveedor(ModeloBase):

    nombre_empresa = models.CharField(
        max_length=100
    )

    nit = models.CharField(
        max_length=20,
        unique=True
    )

    correo = models.EmailField()

    telefono = models.CharField(
        max_length=20
    )

    direccion = models.CharField(
        max_length=150
    )

    activo = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.nombre_empresa


#servicio que ofrece el proveedor
class ServicioProveedor(ModeloBase):

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE
    )

    nombre_servicio = models.CharField(
        max_length=100
    )

    descripcion = models.TextField()

    precio_referencia = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fecha_disponibilidad = models.DateField()

    activo = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.nombre_servicio


#contrato del proveedor
class ContratoProveedor(ModeloBase):

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT
    )

    numero_contrato = models.CharField(
        max_length=50,
        unique=True
    )

    fecha_inicio = models.DateField()

    fecha_finalizacion = models.DateField()

    monto_contrato = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    vigente = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.numero_contrato