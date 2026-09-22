from rest_framework import viewsets

from .models import (
    Proveedor,
    ServicioProveedor,
    ContratoProveedor
)

from .serializers import (
    ProveedorSerializer,
    ServicioProveedorSerializer,
    ContratoProveedorSerializer
)


class ProveedorViewSet(viewsets.ModelViewSet):

    queryset = Proveedor.objects.all()

    serializer_class = ProveedorSerializer



class ServicioProveedorViewSet(viewsets.ModelViewSet):

    queryset = ServicioProveedor.objects.all()

    serializer_class = ServicioProveedorSerializer



class ContratoProveedorViewSet(viewsets.ModelViewSet):

    queryset = ContratoProveedor.objects.all()

    serializer_class = ContratoProveedorSerializer