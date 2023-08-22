#!/usr/bin/python3
"""
Change making module
"""


def makeChange(coins, total):
		"""
    Makes changes
    """
	  if total <= 0:
        return 0
    sot = total
    coins_compt = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while sot > 0:
        if coin_index >= n:
            return -1
        if sot - sorted_coins[coin_index] >= 0:
            sot -= sorted_coins[coin_index]
            coins_compt += 1
        else:
            coin_index += 1
    return coins_compt
