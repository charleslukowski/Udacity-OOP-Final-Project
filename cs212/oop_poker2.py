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
    def reset_betting(self):
        self.bet_times = 0
        for seat in self.seats:
            player = self.seats[seat]
            if player:
                player.bet_this_hand = 0
                player.taken_turn = False
                if player.sitting_out or player.balance <= 0:
                    player.inhand=False
                else:
                    player.inhand=True
    def betting_round(self):
        self.reset_betting()
        print '='*20
        print 'Betting Round Begins...'
        current_pos = self.seat_math(self.dealer_pos, 1)
        while not self.betting_over():
            #print 'Current: %s' % current_pos
            current = self.seats[current_pos]
            if current == None:
                current_pos = self.seat_math(current_pos, 1)
                current = self.seats[current_pos]
            if current:
                #print 'Player found at %s' % current_pos
                if current.inhand and current.balance >= 0:
                    #print 'Player is in the hand, and balance > 0'
                    if current.type == 'NPC':
                        #print 'Player is an NPC'
                        current.take_action(self, current.get_options(self)[0])
                    else:
                        #print 'Player is human'
                        print current.get_options(self)
                        action = raw_input('Enter your action>>> ')
                        current.take_action(self, action)
                        current_pos = self.seat_math(current_pos, 1)
                        current = self.seats[current_pos]
    def betting_over(self):
        max_bet_level = 0
        for seat in self.seats:
            player = self.seats[seat]
            if player:
                # print '='*20
                # print 'Testing Betting over'
                # print '='*20
                # print 'Player at Position: %s' % seat
                # print 'Player Name: %s' % player.name
                # print 'Player bet this hand: %s' % player.bet_this_hand
                # print 'Player taken turn?: %s' % player.taken_turn
                # print 'Max Bet Level: %s' % max_bet_level
                #Betting would be over if all player bets match
                if player.bet_this_hand >= max_bet_level and player.taken_turn:
                    max_bet_level = player.bet_this_hand
                    # print 'Player is above max bet level'
                    # print 'New Max Bet Level: %s' % max_bet_level
        # print 'Reviewed all players and max bet is: %s' % max_bet_level
        # print 'Now checking if all players bets match'
        # print '-'*20
        for seat in self.seats:
            player = self.seats[seat]
            if player:
                #Betting would be over if all player bets match
                # print 'Player at Position: %s' % seat
                # print 'Player Name: %s' % player.name
                # print 'Player bet this hand: %s' % player.bet_this_hand
                # print 'Player taken turn?: %s' % player.taken_turn
                # print 'Max Bet Level: %s' % max_bet_level
                if not player.taken_turn:
                    # print 'Player %s has not taken turn yet' % player.name
                    return False
                elif player.bet_this_hand <> max_bet_level and player.inhand:
                    # print 'Players bet does not match, and they are still in the hand'
                    # print 'Betting is not over...'
                    return False
                else:
                    # print 'Players bets match the max'
                    pass
        return True


        print 'Betting Over'
        return False
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
        self.bet_this_hand = 0

    def sit_in(self, table, seat):
        table.seats[seat] = self
        self.sitting_out = False

    def take_action(self, table, action):
        """Perform either Check, Bet, Call, Raise, Fold within
        the context of the betting round
        """
        print '#'*20
        print 'Action taken by %s is %s' % (self.name, action)
        print '#'*20
        if action == 'Check':
            self.taken_turn = True
            self.inhand = True
            self.balance = self.balance
        elif action == 'Bet':
            self.taken_turn = True
            self.inhand = True
            bet_amt = table.get_bet_amt()
            self.balance -= bet_amt
            self.bet_this_hand += bet_amt
            table.pot += bet_amt
            table.current_bet = bet_amt
            table.bet_times +=1
        elif action == 'Call':
            self.taken_turn = True
            self.inhand = True
            self.balance -= table.current_bet
            self.bet_this_hand += table.current_bet
            table.pot += table.current_bet
        elif action == 'Raise':
            self.taken_turn = True
            self.inhand = True
            raise_amt = table.get_raise_amt()
            self.bet_this_hand += raise_amt
            self.balance -= raise_amt
            table.pot += raise_amt
            table.current_bet = raise_amt
        elif action == 'Fold':
            self.taken_turn = True
            self.inhand = False

    def get_options(self, table):
        """Returns a list of options, based on
        status of the hand. If bets have been placed, and what
        level of betting the round is at.
        """
        if table.bet_times == 0:
            print 'Table Bets are 0, so Check is an option'
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

def main():
    d = Deck()
    d.shuffle()
    t = Table(d.card_list, 1, 2)
    p1 = PC('Joe')
    p1.sit_in(t, 0)
    npc1 = NPC('NPC1')
    npc1.sit_in(t, 1)

    t.display()

    t.deal_players(2, 'deal hole cards')

    t.display()

    t.betting_round() # Bet on hole cards

    t.display()

    t.deal_common(3, 'flop')

    t.display()

    t.betting_round() # Bets on the flop

    t.display()

    t.deal_common(1, 'turn')

    t.display()

    t.betting_round() # Bets on the turn

    t.deal_common(1, 'river')

    t.display()

    t.betting_round() # Bets on the river

    t.display()

if __name__ == '__main__':
    main()
