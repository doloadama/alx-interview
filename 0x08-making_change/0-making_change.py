#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total > 0:  # Check if total amount can be made
        return -1

    return num_coins
