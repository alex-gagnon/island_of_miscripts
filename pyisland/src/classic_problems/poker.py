import itertools
import sys
from collections import defaultdict, namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class Hand:
    def __init__(self, hand):
        self.hand = [Card(rank, suit) for rank, suit in hand]


class Poker:
    """ Find a winning Poker hand. 
    Score Card:
        8: Royal Flush* - Ten, Jack, Queen, King, Ace of the same suit
        8: Straight Flush* - Consecutive values of the same suit
        7: Four of a Kind - Four cards of the same value
        6: Full House - Three of a kind and a pair
        5: Flush - All cards of the same suit
        4: Straight - All cards are consecutive values
        3: Three of a Kind - Three cards of the same value
        2: Two Pair - Two different pairs
        1: One Pair - Two cards of the same value
        0: High Card - Highest value card

        * Royal and straight flush are evaluated together as highest value wins.
    """

    ranks = [str(n) for n in range(2, 10)] + list("TJQKA")
    rank_values = {rank: i for i, rank in enumerate(ranks, 2)}

    def __init__(self, hand):
        self.hand = Hand(hand).hand
        self.hand_rank_values = sorted([self.rank_values.get(card.rank) for card in self.hand], reverse=True)
        self.hand_suits = [card.suit for card in self.hand]

    def __str__(self):
        return str(self.hand)
    
    def eval_hand(self):
        # Evaluate for Royal and Straight Flush
        if self.straight_flush(): 
            return 8, self.hand_rank_values[0]
        # Evaluate for Flush
        if self.flush(): 
            return 5, self.hand_rank_values
        # Evaluate for Straight
        if self.straight(): 
            return 4, self.hand_rank_values[1]

        trips = []
        pairs = []
        for v, group in itertools.groupby(self.hand_rank_values):
            # Count for identical hand rank values
            count = sum(1 for _ in group)
            # Evaluate for Four of a Kind
            if count == 4: 
                return 7, v, self.hand_rank_values
            elif count == 3: 
                trips.append(v)
            # Evaluate for Pairs
            elif count == 2: 
                pairs.append(v)
        
        # Evaluate for Full House Three of a Kind
        if trips: 
            return (6 if pairs else 3), trips, pairs, self.hand_rank_values
        # Returns otherwise for Pairs and High Cards
        return len(pairs), pairs, self.hand_rank_values

    def straight_flush(self):
        """ Evaluates for Royal Flush and Straight Flush. """
        return self.straight() and self.flush()

    def flush(self):
        # Reduces card suits into a set
        return len({card.suit for card in self.hand}) == 1

    def straight(self):
        high_card, low_card = max(self.hand_rank_values), min(self.hand_rank_values)
        unique_cards = len(set(self.hand_rank_values))
        # Difference between lowest and highest card in a straight is always 4, unless it's a low-Ace straight
        return (high_card - low_card == 4 and unique_cards == 5) or self.hand_rank_values == [14, 5, 4, 3, 2]
    


def create_player_hands(hands):
    """ Create Poker objects from a string of two hands. Where Player 1
    has the first 5 cards and Player 2 has the other 5 cards.
    Example hand set:
        Test 1: '5H 5C 6S 7S KD 2C 3S 8S 8D TD'
    """
    player_1 = Poker(hands.split()[:5])
    player_2 = Poker(hands.split()[5:])
    return player_1, player_2

def play(hands):
    """ Returns winner from Poker game. """
    player_1, player_2 = create_player_hands(hands)
    winner = "Player 1" if player_1.eval_hand() > player_2.eval_hand() else "Player 2"
    return winner

# Hacker Rank
def run_hacker_rank():
    def get_hands():
        lines = [line.rstrip() for line in sys.stdin.readlines()]
        cases = lines.pop(0)
        return [play(hands) for hands in lines]
    results = get_hands()
    for winner in results:
        print(winner)
