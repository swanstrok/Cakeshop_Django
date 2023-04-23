from rest_framework import serializers

from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор к модели Order"""
    class Meta:
        model = Order
        fields = '__all__'