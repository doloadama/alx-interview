#!/usr/bin/python3
"""
0_making_change
"""


def makeChange(coins, total):
    # Initialize an array to store the minimum number of coins required for each amount
    minCoins = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total amount of 0
    minCoins[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the minimum number of coins for each amount
        for amount in range(coin, total + 1):
            # Choose the minimum between the current minimum and using the current coin
            minCoins[amount] = min(minCoins[amount], minCoins[amount - coin] + 1)

    # Check if the total amount can be met by any number of coins
    if minCoins[total] == float('inf'):
        return -1

    return minCoins[total]
