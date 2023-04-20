from django.test import TestCase

import pytest
from django.contrib.auth.models import User


# Create your tests here.
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('user', 'user@mail.com', '333')
    assert User.objects.count() == 1
