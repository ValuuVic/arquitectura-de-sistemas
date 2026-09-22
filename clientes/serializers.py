from rest_framework import serializers

from .models import Cliente, Direccion, Contacto


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'



class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccion
        fields = '__all__'



class ContactoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacto
        fields = '__all__'