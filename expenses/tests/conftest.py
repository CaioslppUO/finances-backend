# Django
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group

# Pytest
import pytest

# Fixtures de dados
from .fixtures import *

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    group, _ = Group.objects.get_or_create(name="user")

    user = User.objects.create_user(
        username="test_user",
        password="test1234",
    )

    user.groups.add(group)
    return user

@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client