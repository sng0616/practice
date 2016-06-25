# http://www.reddit.com/r/dailyprogrammer/comments/378h44/20150525_challenge_216_easy_texas_hold_em_1_of_3/

import random
from collections import defaultdict

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

deck = []
for i, j in enumerate(numbers):
	for a, b in enumerate(suits):
		card = numbers[i] + " of " + suits[a]
		deck.append(card)

#print deck

players = int(raw_input("How many players? Choose 2-8. "))
hands = {"player": "hand"}
for i in range(0, players):
#	hands["player"] = defaultdict(list)
	hands["player"] = "Player {0}".format(i+1)
	for j in range(0,2):
		hands["hand"] = []
		index = random.randint(1, 52)
		card = deck[index]
		hands["hand"].append(card)
		print hands

# To-do list:
# 1. Create 1 dictionary with 2 keys (player, hand) where the values are "Player #?" and a list of cards for the player's hand