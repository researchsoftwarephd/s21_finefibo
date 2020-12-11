import pytest

@pytest.fixture(scope = 'module')
def return42():
    """Some documentation of our fixture"""
    return 42