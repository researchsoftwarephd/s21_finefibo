import pytest

# def test_failed():
#     assert 0 == 1

# @pytest.mark.skip()
# def test_skipped():
#     pass

# @pytest.mark.xfail()
# def test_should_fail_and_fails():
#     assert 0 == 1

# @pytest.mark.xfail()
# def test_should_fail_but_does_not():
#     assert 1 == 1

def test_return42(return42):
    assert return42 == 42