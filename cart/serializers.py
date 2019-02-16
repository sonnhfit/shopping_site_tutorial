from rest_framework import serializers
from .models import Cart


class AddCartItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)
    cart_id = serializers.IntegerField(required=True)


class CartSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField()
