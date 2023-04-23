from rest_framework import viewsets

from ..models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class ProductAPIViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset