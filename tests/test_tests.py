import pytest

@pytest.mark.skip()
def test_something():
    pass

@pytest.mark.xfail()
def test_that_is_supposed_to_fail():
    assert 4 == 5

def test_return42(return42):
    assert return42 == 42

@pytest.mark.xfail()
def test_return42_fail(return42):
    assert return42 == 24
