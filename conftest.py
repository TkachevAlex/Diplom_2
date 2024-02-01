import pytest
from objects.user import User


@pytest.fixture(scope="function")
def setup():
    user = User()
    user.create_user()
    yield user
    user.delete_user()
