#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): a list of the values of the coins
        total (_type_): is 0 or less return 0

    Returns:
        _type_: _description_
    """
    if total <= 0:
        return 0
    
    # Initialize table
    dp = [float('inf')]*(total+1)
    dp[0] = 0
    
    # Build up table
    for coin in coins:
        for i in range(coin, total+1):
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    
    # Check if total amount can be made
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
