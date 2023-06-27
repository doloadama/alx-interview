#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    # Check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Generate a list of prime numbers up to n
    def get_primes(n):
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    # Simulate a single game
    def play_game(n):
        primes = get_primes(n)
        is_maria_turn = True

        while primes:
            selected_prime = primes.pop(0)
            primes = [num for num in primes if num % selected_prime != 0]
            is_maria_turn = not is_maria_turn

        return "Maria" if is_maria_turn else "Ben"

    # Track the number of wins for each player
    wins = {"Maria": 0, "Ben": 0}

    # Play multiple games
    for n in nums:
        winner = play_game(n)
        wins[winner] += 1

    max_wins = max(wins.values())

    if max_wins == 0 or wins["Maria"] == wins["Ben"]:
        return None

    return max(wins, key=wins.get)
