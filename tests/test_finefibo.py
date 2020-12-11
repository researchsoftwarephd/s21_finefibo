import pytest
from finefibo.finefibo import fibo_number

@pytest.mark.parametrize('n, expected',
    [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (12, 144)])
def test_fibo_number_values(n, expected):
    assert fibo_number(n) == expected

@pytest.mark.fast
@pytest.mark.parametrize('err, val',
    [(ValueError, -1),
    (TypeError, -1.4),
    (TypeError, 'hello world'),
    (TypeError, (1, 3, 4, 5))])
def test_fibo_number_errors(err, val):
    with pytest.raises(err):
        fibo_number(val)
