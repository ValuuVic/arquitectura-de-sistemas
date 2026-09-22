from rest_framework import serializers

from .models import (
    Bodega,
    MovimientoInventario,
    InventarioProducto
)


class BodegaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bodega
        fields = '__all__'



class MovimientoInventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovimientoInventario
        fields = '__all__'



class InventarioProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventarioProducto
        fields = '__all__'