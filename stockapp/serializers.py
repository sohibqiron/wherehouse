from rest_framework import serializers
from .models import *

class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id","name","location"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ShipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
