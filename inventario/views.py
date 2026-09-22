from rest_framework import viewsets

from .models import (
    Bodega,
    MovimientoInventario,
    InventarioProducto
)

from .serializers import (
    BodegaSerializer,
    MovimientoInventarioSerializer,
    InventarioProductoSerializer
)


class BodegaViewSet(viewsets.ModelViewSet):

    queryset = Bodega.objects.all()

    serializer_class = BodegaSerializer



class MovimientoInventarioViewSet(viewsets.ModelViewSet):

    queryset = MovimientoInventario.objects.all()

    serializer_class = MovimientoInventarioSerializer



class InventarioProductoViewSet(viewsets.ModelViewSet):

    queryset = InventarioProducto.objects.all()

    serializer_class = InventarioProductoSerializer