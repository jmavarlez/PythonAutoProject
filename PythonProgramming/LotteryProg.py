"""
Demonstrates:
Lists/Tuples/Sets/Dictionaries
"""


lottery_numbers = {1, 3, 5, 7, 9, 11}

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

winningshigh = 0
for counter, player in enumerate(players):
  num = player["numbers"]
  winnings = 100 ** len(num.intersection(lottery_numbers))
  if winningshigh < winnings:
    winningshigh = winnings
    winner = player["name"]
print (f"{winner} won {winningshigh}.")