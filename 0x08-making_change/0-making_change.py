#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """making changes module"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    coin_count = 0
    current_total = 0

    for coin in coins:
        while current_total + coin <= total:
            current_total += coin
            coin_count += 1

        if current_total == total:
            return coin_count

    return -1
