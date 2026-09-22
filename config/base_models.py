import uuid

from django.db import models


class ModeloBase(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    eliminado = models.BooleanField(
        default=False
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        abstract = True