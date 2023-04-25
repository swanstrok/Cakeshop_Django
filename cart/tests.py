from django.test import TestCase

import pytest
from django.urls import reverse


# Create your tests here.

@pytest.mark.django_db
def test_cart_detail_unauthorized(client):
    url = reverse('cart:cart_detail')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_cart_detail_as_admin(admin_client):
    url = reverse('cart:cart_detail')
    response = admin_client.get(url)
    assert response.status_code == 200