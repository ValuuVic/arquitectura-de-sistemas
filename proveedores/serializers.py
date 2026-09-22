from rest_framework import serializers

from .models import (
    Proveedor,
    ServicioProveedor,
    ContratoProveedor
)


class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = '__all__'



class ServicioProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicioProveedor
        fields = '__all__'



class ContratoProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContratoProveedor
        fields = '__all__'