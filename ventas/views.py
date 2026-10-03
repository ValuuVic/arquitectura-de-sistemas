from rest_framework import viewsets

from .models import OrdenCompra, DetalleOrden, Factura

from .serializers import (
    OrdenCompraSerializer,
    DetalleOrdenSerializer,
    FacturaSerializer
)


class OrdenCompraViewSet(viewsets.ModelViewSet):

    queryset = OrdenCompra.objects.all()

    serializer_class = OrdenCompraSerializer



class DetalleOrdenViewSet(viewsets.ModelViewSet):

    queryset = DetalleOrden.objects.all()

    serializer_class = DetalleOrdenSerializer



class FacturaViewSet(viewsets.ModelViewSet):

    queryset = Factura.objects.all()

    serializer_class = FacturaSerializer