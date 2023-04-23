from rest_framework import viewsets

from ..models import Order
from .serializers import OrderSerializer


class OrderAPIViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset


class OrderPaidAPIViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.filter(is_paid=True)
        return queryset