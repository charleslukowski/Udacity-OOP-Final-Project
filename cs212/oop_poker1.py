#OOP Poker - Based on CS ___ Udacity Poker Problem, with OOP concepts

import random


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
		self.bet_level = 1
		self.current_bet = 0
		self.bet_times = 0
		self.pot = 0
		self.cards = cards
		self.round = 1
		self.common_cards = []
		self.seats = {} # Dictionary of player locations
		for i in range(self.positions):
			self.seats[i] = None
	def get_bet_amt(self):
		if self.bet_level == 1:
			return self.bet_level * self.min_bet * 1
		elif self.bet_level > 1:
			return 2 * self.min_bet * 1
	def get_raise_amt(self):
		return 2 * self.get_bet_amt()

	def deal_players(self, n, state):
		self.state = state
		for seat in self.seats:
			if self.seats[seat] == None:
				pass
				#print 'Skipping seat: %d' % seat
			else:
				for i in range(n):
					self.seats[seat].cards.append(self.cards.pop())
					self.seats[seat].inhand = True

	def deal_common(self, n, state):
		self.state = state
		for i in range(n):
			self.common_cards.append(self.cards.pop())

	def display_open_seats(self):
		open_seats = []
		for i in self.seats:
			if self.seats[i] == None:
				open_seats.append(i)
		return 'Open seats at the following positions:\n%s' % open_seats

	def seat_math(self, position, change):
		"""Given a position, and the change in position returns 
		a new position at the table. Needed to go around the table.
		"""
		max_pos = max(self.seats.keys())
		min_pos = min(self.seats.keys())
		pos_new = position + change
		if pos_new > max_pos:
			# if pos_new = 8 -----> 0 == -1 + (pos_new - max_pos)
			return -1 + (pos_new - max_pos)
		elif pos_new < min_pos:
			return max_pos + 1 + pos_new
		else:
			return pos_new

	def betting_round(self):
		current_pos = self.seat_math(self.dealer_pos, 1)
		# current = self.seats[current_pos]
		# while current == None:
		# 	current_pos = self.seat_math(current_pos, 1)
		# 	current = self.seats[current_pos]
		# while current.inhand and current.taken_turn == False:
		# 	if current.type == 'NPC':
		# 		current.take_action(self, current.get_options(self)[0]) 
		# 	else:
		# 		print current.get_options(self)
		# 		action = raw_input('Enter your action')
		# 		current.take_action(self, action)
		for seat in self.seats:
			if self.seats[current] and current.inhand and current.taken_turn = False: # If a player in the seat
				print 'ok'
			else:
				print 'not ok'


	def display(self):
		print 'Table Status: %s' % self.state
		print '-'*63
		print 'Round: %d \t Pot: %d \t' % (self.round, self.pot)
		print '='*63
		seat_names = []
		seat_balances = []
		seat_cards = []
		common_cards = []
		common_card_output = ''

		seat_number = ''
		seat_type = ''
		for key in self.seats.keys():
			#Display for seat numbers
			if seat_number == '':
				seat_number += 'Seat:' + str(key)
			else:
				seat_number += '\tSeat:' + str(key)

			# Display for table positions (Dealer button, etc)
			if key == self.dealer_pos:
				seat_type += 'D\t'
			elif key == self.seat_math(self.dealer_pos, -1):
				seat_type += 'BB\t'
			elif key == self.seat_math(self.dealer_pos, -2):
				seat_type += 'LB\t'
			else:
				seat_type += '\t'
		if self.common_cards:
			for card in self.common_cards:
				common_cards.append(card.simple_name_card(card.suit, card.rank))
			common_card_output = ' - '.join(common_cards)
			
		for index, seat in enumerate(self.seats):
			if self.seats[seat]:
				seat_names.append(self.seats[seat].name)
				seat_balances.append(str(self.seats[seat].balance))
				if self.seats[seat].cards:
					player_cards = []
					for card in self.seats[seat].cards:
						player_cards.append(card.simple_name_card(card.suit, card.rank))
					seat_cards.append('-'.join(player_cards))
			else:
				seat_names.append('------')
				seat_balances.append('0')
				seat_cards.append('--')
		print 'Common: \t %s' % common_card_output
		print seat_number
		print seat_type
		print '\t'.join(seat_names)
		print '\t'.join(seat_balances)
		print '\t'.join(seat_cards)


class Player(object):
	"""Player (PC/NPC) parent class. Contains properties that are common to 
	both PC/NPC players. 
	Required: Name, Starting Funds
	"""
	def __init__(self, name, balance=100):
		self.name = name
		self.balance = balance
		self.sitting_out = True
		self.cards = []
		self.inhand = False
		self.taken_turn = False

	def sit_in(self, table, seat):
		table.seats[seat] = self
		self.sitting_out = False

	def take_action(self, table, action):
		"""Perform either Check, Bet, Call, Raise, Fold within
		the context of the betting round
		"""
		print 'Action taken %s' % action
		if action == 'Check':
			self.taken_turn = True
			self.inhand = True
			self.balance = self.balance
		elif action == 'Bet':
			self.taken_turn = True
			self.inhand = True
			bet_amt = table.get_bet_amt()
			self.balance -= bet_amt
			table.pot += bet_amt
			table.current_bet = bet_amt
		elif action == 'Call':
			self.taken_turn = True
			self.inhand = True
			self.balance -= table.current_bet
			table.pot += table.current_bet
		elif action == 'Raise':
			self.taken_turn = True
			self.inhand = True
			raise_amt = table.get_raise_amt()
			self.balance -= raise_amt
			table.pot += raise_amt
			table.current_bet = raise_amt
		elif action == 'Fold':
			self.taken_turn = True
			self.inhand = False

	def get_options(self, table):
		"""Returns a list/dictionary (???) of options, based on 
		status of the hand. If bets have been placed, and what
		level of betting the round is at.
		"""
		if table.bet_times == 0:
			return ['Check', 'Bet', 'Fold']
		else:
			if table.bet_times <= 4:
				return ['Call', 'Raise', 'Fold']
			else:
				return ['Call', 'Fold']


class NPC(Player):
	"""Subclass of Player. NPC (Non-Player Character) is a computer player.
	Needs to make basic decisions
	based on ratios, does not use input, performs actions
	based on code-only"""
	def __init__(self, name):
		Player.__init__(self, name)
		self.type = 'NPC'
class PC(Player):
	"""Subclass of Player. PC (Player Character) is a human player, and needs to be presented 
	with each decision and perform that action using some type of input.
	"""
	def __init__(self, name):
		Player.__init__(self, name)
		self.type = 'PC'
		
		
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
		self.rank_letters = {1 : 'A',
							2: '2',
							3: '3',
							4: '4',
							5: '5',
							6: '6',
							7: '7',
							8: '8',
							9: '9', 
							10:'T',
							11:'J',
							12:'Q',
							13:'K'}

	def name_card(self, suit, rank):
		"""Returns the card in written form ie. Ace of Diamonds"""
		return '%s of %s' % (self.rank_names[rank], self.suit_names[suit])

	def simple_name_card(self, suit, rank):
		return self.rank_letters[rank] + suit

class Deck(object):
	"""Standard deck of playing cards"""
	def __init__(self):
		"""
		When a deck is created, create and append cards to the card_list
		"""
		self.suits = ['D', 'H', 'C', 'S']
		self.ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
		
		self.card_list = []
		for suit in self.suits:
			for rank in self.ranks:
				self.card_list.append(Card(suit, rank))
	def shuffle(self):
		random.shuffle(self.card_list)
	def display(self):
		for card in self.card_list:
			print card.simple_name_card(card.suit, card.rank)
