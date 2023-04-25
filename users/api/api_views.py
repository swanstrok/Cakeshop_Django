from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import UserSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'date_joined']

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
