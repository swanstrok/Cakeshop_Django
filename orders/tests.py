import pytest
from django.urls import reverse


# Create your tests here.
@pytest.mark.django_db
def test_order_add_unauthorized(client):
    url = reverse('orders:order_add')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_order_add_as_admin(admin_client):
    url = reverse('orders:order_add')
    response = admin_client.get(url)
    assert response.status_code == 200
