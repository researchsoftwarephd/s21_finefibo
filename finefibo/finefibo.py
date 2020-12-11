"""
An awesome Python module for obtaining Fibonacci numbers.
"""

def fibo_number(n: int) -> int:
    """Returns the n-th Fibonacci number.

    Arguments:

    n -- The index of the desired number in the Fibonacci sequence.

    Returns:

    The n-th Fibonacci number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_number(n - 1) + fibo_number(n - 2)
