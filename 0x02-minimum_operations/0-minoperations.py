#!/usr/bin/env python3
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
    # return 0 if n is less than or equal to 0, which means it is impossible to achieve
    if n <= 0:
        return 0
    # start checking from 2 as the first prime number
    i = 2
    count = 0
    # loop until i is less than or equal to n
    while i <= n:
        # check if n is divisible by i
        while n % i == 0:
            # increment the count by 1 for each division
            count += 1
            # divide n by i and update n
            n = n // i
        # increment i by 1
        i += 1
    # return the count which is the minimum number of operations needed
    return count
