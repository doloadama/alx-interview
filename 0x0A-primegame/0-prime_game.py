#!/usr/bin/python3
"""
prime game test
"""


def isWinner(x, nums):
  """
  Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

  They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

  Prototype: def isWinner(x, nums)
  where x is the number of rounds and nums is an array of n
  Return: name of the player that won the most rounds
  If the winner cannot be determined, return None
  You can assume n and x will not be larger than 10000
  You cannot import any packages in this task
  """

  maria_wins = 0
  ben_wins = 0
  for _ in range(x):
    nums = [n for n in nums if isPrime(n)]
    if len(nums) == 0:
      if maria_wins == ben_wins:
        return None
      else:
        return "Ben"
    elif nums[0] % 2 == 0:
      winner = "Ben"
    else:
      winner = "Maria"
    if winner == "Maria":
      maria_wins += 1
    else:
      ben_wins += 1
  return "Maria" if maria_wins > ben_wins else "Ben"

def isPrime(n):
  """
  Returns True if n is a prime number, False otherwise.
  """

  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

if __name__ == "__main__":
  print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
