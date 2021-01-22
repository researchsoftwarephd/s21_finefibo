# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Author: Nuno Fachada

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

    # Is the parameter a int?
    if not isinstance(n, int):
        raise TypeError('Parameter n must an integer')

    # Is the value non-negative?
    if n < 0:
        raise ValueError('Parameter n must be non-negative')

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_number(n - 1) + fibo_number(n - 2)
