from rest_framework import viewsets

from ..models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    """Отображает api всех категорий товаров и дает возможность отображать их по одной"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class ProductAPIViewSet(viewsets.ModelViewSet):
    """Отображает api всех товаров и дает возможность отображать их по одному.
     С возможностью фильтрации по полям 'available' и 'category' и сортировки по полю 'id'"""
    serializer_class = ProductSerializer
    filterset_fields = ['available', 'category']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
