class Card(object):
	def __init__(self, suit, rank):
		"""
		Create a single playing card
		suit: (str) D, H, C, or S
		rank: (int) 1 - 13 (Ace first, King last)
		"""
		self.suit = suit
		self.rank = rank
		self.suit_names = { 'D' : 'Diamonds',
							'H' : 'Hearts',
							'C' : 'Clubs',
							'S' : 'Spades'}
		self.rank_names = {1 : 'Ace',
							2: 'Two',
							3: 'Three',
							4: 'Four',
							5: 'Five',
							6: 'Six',
							7: 'Seven',
							8: 'Eight',
							9: 'Nine', 
							10:'Ten',
							11:'Jack',
							12:'Queen',
							13:'King'}
		def name_card(self, suit, rank):
			"""Returns the card in written form ie. Ace of Diamonds"""
			return '%s of %s' % (self.rank_names[rank], self.suit_names[suit])

class Deck(object):
	def __init__(self):
		"""Creates a deck of cards"""
		self.ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		self.suits = ['D', 'H', 'C', 'S']
		
		self.card_list = []
		for i in self.suits:
			for j in self.ranks:
				self.card_list.append(Card(i,j))
	# def create_card(self, suit, rank):
	# 	return (suit, rank)
	

deck1 = Deck()
print deck1.name_card('D', 1)