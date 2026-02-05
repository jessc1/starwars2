import pytest

from core.models import User

test_user = {
    "username": "user_test",
    "email": "test@email.com",
    "password": "testpasswd"
}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_superuser(**test_user)


