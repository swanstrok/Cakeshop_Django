from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
