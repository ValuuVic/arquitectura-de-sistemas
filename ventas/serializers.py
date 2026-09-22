from rest_framework import serializers

from .models import OrdenCompra, DetalleOrden, Factura


class OrdenCompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdenCompra
        fields = '__all__'



class DetalleOrdenSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleOrden
        fields = '__all__'



class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = '__all__'