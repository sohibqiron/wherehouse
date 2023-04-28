from rest_framework import serializers
from .models import *
from stockapp.models import *
from stockapp.serializers import *
from userapp.serializers import *

class CartSerializer(serializers.ModelSerializer):
    customer = CustomUserSerializer(read_only=True)
    # used to represent the target of the relationship using its __unicode__ method
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'customer', 'created_at', 'updated_at', 'items')


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')



class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializers(read_only=True)
    order_items = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'total', 'created_at', 'updated_at', 'order_items')

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order



class OrderItemSerializer(serializers.ModelSerializer):

    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity')