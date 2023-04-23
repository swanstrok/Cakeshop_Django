from rest_framework import serializers

from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор к модели Category"""
    class Meta:
        model = Order
        fields = '__all__'