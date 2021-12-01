import pytest
from finefibo.fibo import fibo_number

@pytest.mark.parametrize(
    'n, expected',
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (12, 144)])
def test_fibo_number_values(n, expected):
    assert fibo_number(n) == expected

@pytest.mark.parametrize(
    'input, exception',
    [(-1, ValueError), (-5000, ValueError),
    (-1.4, TypeError), ('hello world', TypeError), ((1, 2, 3, 4), TypeError)])
def test_fibo_number_errors(input, exception):
    with pytest.raises(exception):
        fibo_number(input)

@pytest.mark.fast
def test_return42(return42):
    assert return42 == 42