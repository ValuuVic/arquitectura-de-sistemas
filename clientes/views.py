from rest_framework import viewsets

from .models import Cliente, Direccion, Contacto
from .serializers import (
    ClienteSerializer,
    DireccionSerializer,
    ContactoSerializer
)


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer



class DireccionViewSet(viewsets.ModelViewSet):

    queryset = Direccion.objects.all()

    serializer_class = DireccionSerializer



class ContactoViewSet(viewsets.ModelViewSet):

    queryset = Contacto.objects.all()

    serializer_class = ContactoSerializer