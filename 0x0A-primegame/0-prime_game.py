#!/usr/bin/python3
"""
0-Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the prime game, where n may be different
    for each round. Assuming Maria always goes first and both players play optimally,
    returns the name of the player that won the most rounds. If the winner cannot be
    determined, returns None.

    Args:
        x (int): The number of rounds to play.
        nums (list): An array of n for each round.

    Returns:
        str or None: The name of the player that won the most rounds, or None if the
            winner cannot be determined.
    """
    # Initialize a variable to keep track of the number of rounds each player wins
    maria_wins = 0
    ben_wins = 0

    # Iterate over each round
    for i in range(x):
        # Get the value of n for this round
        n = nums[i]

        # Create a list of all integers from 2 to n, inclusive
        num_list = list(range(2, n+1))

        # Initialize a variable to keep track of the current player
        current_player = "Maria"

        # Keep looping until there are no more prime numbers in the list
        while True:
            # Find the smallest prime number in the list
            prime = None
            for num in num_list:
                if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
                    prime = num
                    break

            # If no prime number was found, exit the loop
            if prime is None:
                break

            # Remove the prime number and its multiples from the list
            num_list = [num for num in num_list if num % prime != 0]

            # Switch to the other player
            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        # Update the number of rounds each player wins
        if current_player == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner of the game based on the number of rounds each player won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
