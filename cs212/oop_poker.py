class Card(object):
	"""A playing card, consisting of suit and rank"""
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
	def create_card(suit, rank):
		return (suit, rank)
	def name_card(suit, rank):
		return str(rank) + ' of ' + suit_name[suit]
	def simple_name_card(suit, rank):
		return str(rank) + suit

class Deck(object):
	"""A deck of 52 cards to be used in game"""
	def __init__(self):
		"""Creates a deck of cards"""
		self.ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		self.suits = ['D', 'H', 'C', 'S']
		
		self.card_list = []
		for i in self.suits:
			for j in self.ranks:
				self.card_list.append(Card(i,j))
	def shuffle_deck(deck):
		return random.shuffle(deck)
	
class Player(object):
	"""A player of the game. Is dealt cards, makes bets"""
	def __init__(self):
		#self.table
		#self.chair
		self.playing = True
		self.cards = ()
		self.money = 25
class Hand(object):
	"""Collection of 5 cards"""

class NPC(Player):
	"""Subclass of player. Is computer operated. Cards are not known"""
	def __init__(self):
		self.sees_flop = 0.20
		self.aggression = 0.10

class HumanPlayer(Player):
	"""Subclass of player. Cards are shown. Makes decisions with text input"""
	def __init__(Player):

class Dealer(object):
	"""Deals the cards to players, directs the game"""
	def __init__(self):


class Table(object):
	"""Collection of Dealer, Player, and n-NPC's. Holds the state of the game"""
	def __init__(self):
		self.chairs = 8
		self.state = 'New'
		self.pot = 0
		self.min_bet = 1
		self.max_bet = 2
		self.rake = .01
		self.dealer_chair = 1
		self.little_bet = 7
		self.big_bet = 8


#create Table, Dealer, NPC's, HumanPlayer

#Dealer shuffles deck

#Dealer deals cards, starting with left/right of dealer button

#Dealer conducts betting round, starting with left/right dealer
     #Player makes decisions Bet/Check/Fold

#