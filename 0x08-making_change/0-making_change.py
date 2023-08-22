#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    """Initialize an array to store the minimum
       number of coins needed for each value
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value and update the dp array
    for coin in coins:
        for value in range(coin, total + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
