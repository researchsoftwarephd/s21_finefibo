import pytest
# import pytest_console_scripts
from finefibo.fibo import fibo_number, lucas, jacobsthal, pell, run_from_cli

# @pytest_console_scripts
# def test_run_from_cli(script_runner):
#     ret = script_runner.run('pynum', 'fibo', 11)
#     assert ret.success

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

@pytest.mark.parametrize('n, expected', [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18), (7, 29), (8, 47)])
def test_lucas_number_values(n, expected):
    assert lucas(n) == expected

@pytest.mark.parametrize(
    'input, exception',
    [(-1, ValueError), (-5000, ValueError),
    (-1.4, TypeError), ('hello world', TypeError), ((1, 2, 3, 4), TypeError)])
def test_lucas_number_errors(input, exception):
    with pytest.raises(exception):
        lucas(input)

@pytest.mark.parametrize('n, expected', [(0, 0), (1, 1), (2, 2), (3, 5), (4, 12), (5, 29), (6, 70), (7, 169), (8, 408)])
def test_pell_number_values(n, expected):
    assert pell(n) == expected

@pytest.mark.parametrize(
    'input, exception',
    [(-1, ValueError), (-5000, ValueError),
    (-1.4, TypeError), ('hello world', TypeError), ((1, 2, 3, 4), TypeError)])
def test_pell_number_errors(input, exception):
    with pytest.raises(exception):
        pell(input)


@pytest.mark.parametrize('n, expected', [(0, 0), (1, 1), (2, 1), (3, 3), (4, 5), (5, 11), (6, 21), (7, 43), (8, 85)])
def test_jacobsthal_number_values(n, expected):
    assert jacobsthal(n) == expected



@pytest.mark.fast
def test_return42(return42):
    assert return42 == 42


