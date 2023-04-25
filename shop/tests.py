import pytest

from .models import Category


# Create your tests here.

@pytest.mark.django_db
def test_category_create():
    """Тест на создание новой категории"""
    Category.objects.create(name='Фрукты', slug='frukti')
    assert Category.objects.count() == 1
