#! /usr/bin/env python

# tarot.py

import random


def main():
	tarot = Tarot()
	cards = []

	print("{0} cards in the deck".format(len(tarot.cards)))

	for _ in range(3):
		card = tarot.draw_random_card()
		print("{0} {1}".format(card.suit, card.rank))
		cards.append(card)

	print("{0} cards in the deck".format(len(tarot.cards)))


class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank


class Tarot():
	def __init__(self):
		self.suits = ['wands', 'coins', 'cups', 'swords']
		self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'P', 'KN', 'Q', 'KI']
		
		self.cards = []

		for suit in self.suits:
			for rank in self.ranks:
				card = Card(suit, rank)
				self.cards.append(card)


	def random_card(self):
		index = random.randint(1, len(self.cards)) - 1
		card = self.cards[index]
		return card


	def draw_random_card(self):
		card = self.random_card()
		self.cards.remove(card)
		return card


if __name__ == "__main__":
    main()
