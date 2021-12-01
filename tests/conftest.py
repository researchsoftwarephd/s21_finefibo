import pytest

@pytest.fixture(scope="session")
def return42():
    "Basic fixture with produces the number 42"
    return 42