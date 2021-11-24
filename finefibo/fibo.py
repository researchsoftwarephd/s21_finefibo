"""
An awesome Python module for obtaining Fibonacci numbers.
"""

import sys

def fibo_number(n):
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

def run_from_cli():
    """Called from the command-line, prints the specified Fibonacci number."""

    n = int(sys.argv[1])
    print(fibo_number(n))