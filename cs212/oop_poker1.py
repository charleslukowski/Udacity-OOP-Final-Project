#OOP Poker - Based on CS ___ Udacity Poker Problem, with OOP concepts

class Table(object):
	"""Dealer/Table controlled by this class. Holds a listing of players,
	both PC/NPC at the table. Deals cards and collects the pot. Distributes
	to winning hand.
	Required: min_bet/max_bet (ie. .50/1.00, 1.00/2.00)
	"""
	def __init__(self, min_bet, max_bet, dealer_pos=1, positions=8, state="new"):
		self.min_bet = min_bet
		self.max_bet = max_bet
		self.dealer_pos = dealer_pos
		self.positions = positions
		self.state = state
		self.pot = 0

class Player(object):
	"""Player (PC/NPC) parent class. Contains properties that are common to 
	both PC/NPC players. 
	Required: Name, Starting Funds
	"""
	def __init__(self, name, balance=100):
		self.name = name
		self.balance = balance
		
