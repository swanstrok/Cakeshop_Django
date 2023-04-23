from rest_framework import serializers

from ..models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор к модели Category"""
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор к модели Product"""
    class Meta:
        model = Product
        fields = '__all__'
