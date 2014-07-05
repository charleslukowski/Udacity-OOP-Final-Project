#OOP Poker - Based on CS ___ Udacity Poker Problem, with OOP concepts

class Table(object):
	"""Dealer/Table controlled by this class. Holds a listing of players,
	both PC/NPC at the table. Deals cards and collects the pot. Distributes
	to winning hand.
	Required: min_bet/max_bet (ie. .50/1.00, 1.00/2.00)
	"""
	def __init__(self, cards, min_bet, max_bet, dealer_pos=1, positions=8, state="new"):
		self.min_bet = min_bet
		self.max_bet = max_bet
		self.dealer_pos = dealer_pos
		self.positions = positions
		self.state = state
		self.pot = 0
		self.cards = cards
		self.round = 1
		self.seats = {} # Dictionary of player locations
		for i in range(self.positions):
			self.seats[i] = None

	def display_open_seats(self):
		open_seats = []
		for i in self.seats:
			if self.seats[i] == None:
				open_seats.append(i)
		return 'Open seats at the following positions:\n%s' % open_seats

	def display(self):
		print 'Table Status'
		print '-'*60
		print 'Round: %d \t Pot: %d \t' % (self.round, self.pot)
		print '='*60
		seat_names = []
		seat_balances = []

		for index, seat in enumerate(self.seats):
			if self.seats[seat]:
				seat_names.append(self.seats[seat].name)
				seat_balances.append(str(self.seats[seat].balance))
			else:
				seat_names.append('---')
				seat_balances.append('0')
		print '\t'.join(str(self.seats.keys()))
		print '\t'.join(seat_names)
		print '\t'.join(seat_balances)


class Player(object):
	"""Player (PC/NPC) parent class. Contains properties that are common to 
	both PC/NPC players. 
	Required: Name, Starting Funds
	"""
	def __init__(self, name, balance=100):
		self.name = name
		self.balance = balance
		self.sitting_out = True

	def sit_in(self, table, seat):
		table.seats[seat] = self
		self.sitting_out = False

class NPC(Player):
	"""Subclass of Player. Needs to make basic decisions
	based on ratios, does not use input, performs actions
	based on code-only"""
	def __init__(self, name):
		Player.__init__(self, name)
class PC(Player):
	"""Subclass of Player. Player is a human player, and needs to be presented 
	with each decision and perform that action using some type of input.
	"""
	def __init__(self, name):
		Player.__init__(self, name) 
		
		
class Card(object):
	"""Individual playing card"""
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.suit_names = { 'D': 'Diamonds',
							'H': 'Hearts',
							'C': 'Clubs',
							'S': 'Spades'}
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

	def simple_name_card(self, suit, rank):
		return str(rank) + suit

class Deck(object):
	"""Standard deck of playing cards"""
	def __init__(self):
		self.suits = ['D', 'H', 'C', 'S']
		self.ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
		
		self.card_list = []
		for suit in self.suits:
			for rank in self.ranks:
				self.card_list.append(Card(suit, rank))
	def shuffle_deck(self):
		return random.shuffle(deck)
