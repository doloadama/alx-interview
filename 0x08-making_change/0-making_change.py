#!/usr/bin/python3

def makeChange(coins, total):
  """
  Returns the fewest number of coins needed to meet a given amount total.

  Args:
    coins: A list of the values of the coins in your possession.
    total: The amount of money you need to make change for.

  Returns:
    The fewest number of coins needed to meet total.
    If total is 0 or less, returns 0.
    If total cannot be met by any number of coins you have, returns -1.
  ddd
  """

  if total <= 0:
    return 0

  dp = [float("inf") for _ in range(total + 1)]
  dp[0] = 0

  for coin in coins:
    for i in range(coin, total + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)

  return dp[total] if dp[total] != float("inf") else -1
