import pytest
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.
@pytest.mark.django_db
def test_user_create():
    """Тест создания нового пользователя"""
    User.objects.create_user('user', 'user@mail.com', '333')
    assert User.objects.count() == 1


