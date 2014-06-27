"""
create a deck of cards
add deck to list of cards
remove card from deck
pick a random card from deck
create player
deal card to players hand
"""
import random

rank_global = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suit_global = ['D', 'H', 'C', 'S']
suit_name = {'D' : 'Diamonds',
			 'H' : 'Hearts',
			 'C' : 'Clubs',
			 'S' : 'Spades'}
rank_name = {1: 'A',
			 2: '2',
			 3: '3',
			 4: '4',
			 5: '5',
			 6: '6',
			 7: '7',
			 8: '8',
			 9: '9',
			 10: '10',
			 11: 'J',
			 12: 'Q',
			 13: 'K'}

def create_deck(suit, rank):
	card_list = []
	for i in suit:
		for j in rank:
			card_list.append(create_card(i, j))
	return card_list

def shuffle_deck(deck):
	return random.shuffle(deck)

def create_card(suit, rank):
	return (suit, rank)

def name_card(suit, rank):
	return str(rank) + ' of ' + suit_name[suit]

def simple_name_card(suit, rank):
	return str(rank) + suit

def deal(player):
	player.append(deck.pop())

def deal1(player):
	return deck.pop()

def deal_rounds(players, n):
	"""Deal n to each player"""
	for player in players:
		for i in range(n):
			deal(player)

def display_card(card):
	return rank_name[card[1]] + card[0]

def display(player):
	header = ""
	body = ""
	for i in range(len(player)):
		header += str(i) + '\t'
		body += display_card(player[i]) + '\t'
	return header + '\n' + body
def check_n_cards(player, n):
	"""Returns True if a pair is found, false if not"""
	card_ranks = []
	for card in player:
		card_ranks.append(card[1])
	for card in card_ranks:
		if card_ranks.count(card) > (n-1):
			return True
	return False

def check_flush(player):
	"""Returns True if a flush is found, false if not"""
	card_suits = []
	for card in player:
		card_suits.append(card[0])
	for card in card_suits:
		if card_suits.count(card) > 4:
			return True
	return False

def discard(player, list_of_cards):
	"""Discard cards based on a list of index positions, 0-4"""
	for card in list_of_cards:
		player[card] = deal1(player)
	return player


if __name__ == '__main__':

	player1 = []

	players = [player1]
	deck = create_deck(suit_global, rank_global)
	shuffle_deck(deck)

	deal_rounds(players, 5)
	print 'Player1'
	print display(player1)
	print 'Flush?\t\t' + str(check_flush(player1))
	print '4 of Kind?\t' + str(check_n_cards(player1, 4))
	print '3 of Kind?\t' + str(check_n_cards(player1, 3))
	print 'Pair?\t\t' + str(check_n_cards(player1, 2))
	print 

	temp = raw_input('Enter the positions you want to discard (ex: 012)\n')
	list_to_discard = list(temp)
	for index, value in enumerate(list_to_discard):
		list_to_discard[index] = int(value)

	print list_to_discard
	#list_to_discard = [0,1,2] #for debugging
	player1 = discard(player1, list_to_discard)
	print 

	print 'Player1'
	print display(player1)
	print 'Flush?\t\t' + str(check_flush(player1))
	print '4 of Kind?\t' + str(check_n_cards(player1, 4))
	print '3 of Kind?\t' + str(check_n_cards(player1, 3))
	print 'Pair?\t\t' + str(check_n_cards(player1, 2))
