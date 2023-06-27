#!/usr/bin/python3
"""
prime game
"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of each game."""
    if not nums:
        return None

    def count_primes(n):
        """Count the number of primes in a given range."""
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)

        # Alternate turns between Maria and Ben
        current_player = "Maria"
        while prime_count > 0:
            if current_player == "Maria":
                prime = 2
                while prime <= n:
                    if is_prime(prime):
                        prime_count -= 1
                        break
                    prime += 1
                current_player = "Ben"
            else:
                prime = 2
                while prime <= n:
                    if is_prime(prime):
                        prime_count -= 1
                        break
                    prime += 1
                current_player = "Maria"

        if current_player == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
