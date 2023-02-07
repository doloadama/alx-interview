#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n: int) -> int:
    """n a text file, there is a single character H. Your text editor can execute only two
    operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations

