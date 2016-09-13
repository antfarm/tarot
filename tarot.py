#! /usr/bin/env python

# tarot.py

import random


def main():
	tarot = Tarot()
	cards = []

	print("{0} cards in the deck".format(len(tarot.cards)))

	for _ in range(3):
		card = tarot.draw_random_card()
		cards.append(card)

	print("{0} cards in the deck".format(len(tarot.cards)))

	for card in cards:
		print(card.to_string())


class Card():
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def to_string(self):
		return "{0}: {1}".format(self.name, self.description)


class MinorCard(Card):
	suits = ['wands', 'coins', 'cups', 'swords']
	ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'P', 'KN', 'Q', 'KI']

	def __init__(self, suit, rank, name, description):
		Card.__init__(self, name, description)
		self.suit = suit
		self.rank = rank

	@staticmethod
	def all_cards():  # todo: read card data from json file
		cards = []
		for suit in MinorCard.suits:
			for rank in MinorCard.ranks:
				card = MinorCard(suit, rank, "n/a", "n/a")
				cards.append(card)
		return cards

	def to_string(self):
		return "[{0}|{1}] {2}: {3}".format(self.suit, self.rank, self.name, self.description)


class MajorCard(Card):
	names = list(range(23))

	def __init__(self, name, description):
		Card.__init__(self, name, description)

	@staticmethod
	def all_cards(): # todo: read card data from json file
		cards = []
		for name in MajorCard.names:
			card = MajorCard(name, "n/a")
			cards.append(card)
		return cards

	def to_string(self):
		return "{0}: {1}".format(self.name, self.description)


class Tarot():
	def __init__(self):
		self.cards = MajorCard.all_cards() + MinorCard.all_cards()

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
