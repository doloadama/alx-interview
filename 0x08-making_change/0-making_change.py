#!/usr/bin/python3
# 0_making_change


def makeChange(coins, total):
    """
    coins is a list of coins to change
    total is the amount you need to reach using the
    fewest number of coins
    """
    if total <= 0:
        return 0
    
    #Initialization of an array to store the minimum of coins
    store = [float('inf')] * (total + 1)

    #Base
    store [0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                store[i] = min(store[i], 1+ store[i - coin])

    if store[total] == float('inf'):
        return -1
    
    return store[total]
