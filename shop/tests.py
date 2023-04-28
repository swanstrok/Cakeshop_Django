import pytest
from django.urls import reverse

from .models import Category


# Create your tests here.

@pytest.mark.django_db
def test_category_create():
    """Тест на создание новой категории"""
    Category.objects.create(name='Фрукты', slug='frukti')
    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_product_list_unauthorized(client):
    """Тест отображения продукции для неавторизованного пользователя"""
    url = reverse('shop:product_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_list_as_admin(admin_client):
    """Тест отображения продукции для администратора"""
    url = reverse('shop:product_list')
    response = admin_client.get(url)
    assert response.status_code == 200