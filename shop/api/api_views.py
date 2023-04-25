from rest_framework import viewsets

from ..models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    """Отображает все категории товаров и дает возможность оторажать их по одной"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class ProductAPIViewSet(viewsets.ModelViewSet):
    """Отображает все товары и дает возможность оторажать их по одному"""
    serializer_class = ProductSerializer
    filterset_fields = ['available', 'category']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset