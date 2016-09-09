#! /usr/bin/env python

# tarot.py

import random


def main():
	tarot = Tarot()
	cards = []

	print("{0} cards in the deck".format(len(tarot.cards)))

	for _ in range(3):
		card = tarot.draw_random_card()
		print(card.to_string())
		cards.append(card)

	print("{0} cards in the deck".format(len(tarot.cards)))


class Card():
	TYPE_MIN = 0
	TYPE_MAJ = 1

	def __init__(self, type):
		self.type = type

	def to_string(self):
		if self.type == Card.TYPE_MIN:
			return "{0} {1}".format(self.suit, self.rank)
		elif self.type == Card.TYPE_MAJ:
			return self.name


class MinorCard(Card):
	suits = ['wands', 'coins', 'cups', 'swords']
	ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'P', 'KN', 'Q', 'KI']

	def __init__(self, suit, rank):
		self.type = Card.TYPE_MIN
		self.suit = suit
		self.rank = rank

	@staticmethod
	def all_cards():
		cards = []
		for suit in MinorCard.suits:
			for rank in MinorCard.ranks:
				card = MinorCard(suit, rank)
				cards.append(card)
		return cards


class MajorCard(Card):
	names = list(range(23)) # todo: list of names as strings

	def __init__(self, name):
		self.type = Card.TYPE_MAJ
		self.name = name

	@staticmethod
	def all_cards():
		cards = []
		for name in MajorCard.names:
			card = MajorCard(name)
			cards.append(card)
		return cards


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
