from django.test import TestCase

from django.test import Client
from http import HTTPStatus
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.c = Client()

    def test_is_ok_page_login(self):
        response = self.c.get('/accounts/login/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        response = self.c.get('/accounts/register/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login_user(self):
        credentials = {
            'username': 'Ivan Login',
            'password': 'abrakadabra'
        }
        user = User.objects.create_user(**credentials)
        response = self.c.post('/accounts/login/', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_create_user(self):
        user = User.objects.create_user(
            username='TestIvan',
            email='ivan@mail.com',
            password='4ABefef3rgVM',
        )
        self.assertIsInstance(user, User)

    def test_register_user(self):
        data = {
            'username': 'TestIvan',
            'email': 'ivan@mail.com',
            'password': '4ABefef3rgVM',
            'password_confirmation': '4ABefef3rgVM',
        }

        response = self.c.post('/accounts/register/', data)

        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        user = User.objects.get(username=data['username'])

        self.assertIsInstance(user, User)

# import pytest
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# # Create your tests here.
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('user', 'user@mail.com', '333')
#     assert User.objects.count() == 1
#
#
#
# @pytest.mark.django_db
# def test_view_unauthorized(client):
#     url = reverse('shop:product_list')
#     response = client.get(url)
#     assert response.status_code == 401
#
#
# @pytest.mark.django_db
# def test_view_as_admin(admin_client):
#     url = reverse('shop:product_list')
#     response = admin_client.get(url)
#     assert response.status_code == 200
