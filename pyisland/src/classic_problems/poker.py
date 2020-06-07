from collections import defaultdict, namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class Hand:
    def __init__(self, hand):
        self.hand = [Card(rank, suit) for rank, suit in hand]


class Poker:
    """ Find a winning Poker hand. """

    ranks = [str(n) for n in range(2, 10)] + list("TJQKA")
    rank_values = {rank: i + 2 for i, rank in enumerate(ranks)}

    def __init__(self, hand):
        self.hand = Hand(hand).hand
        self.hand_ranks = self.rank_hand()

    def __str__(self):
        return str(self.hand)
    
    def rank_hand(self):
        ranks = ['..23456789TJQKA'.index(rank) for rank, suit in self.hand]
        ranks.sort(reverse=True)
        # Handle Ace rank as lowest value card
        return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

    def count_values(self):
        values = [card.rank for card in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        return value_counts

    def find_best_hand(self):
        """ Returns the best possible win with current hand. """
        winning_hands = {
            0: {
                "name": "High Card",
                "function": self.high_card
            },
            1: {
                "name": "One Pair",
                "function": self.one_pair
            },
            2: {
                "name": "Two Pairs",
                "function": self.two_pairs
            },
            3: {
                "name": "Three of a Kind",
                "function": self.three_of_a_kind
            },
            4: {
                "name": "Straight",
                "function": self.straight
            },
            5: {
                "name": "Flush",
                "function": self.flush
            },
            6: {
                "name": "Full House",
                "function": self.full_house
            },
            7: {
                "name": "Four of a Kind",
                "function": self.four_of_a_kind
            },
            8: {
                "name": "Straight Flush",
                "function": self.straight_flush
            },
            9: {
                "name": "Royal Flush",
                "function": self.royal_flush
            }
        }
        for k, v in reversed(winning_hands.items()):
            if v['function']():
                return k, v['name'], self.hand_ranks

    def royal_flush(self):
        ranks = [card for card in self.hand if card.rank not in [str(n) for n in range(2, 10)]]
        return len(ranks) == 5 and self.straight_flush()

    def straight_flush(self):
        return self.flush() and self.straight()

    def four_of_a_kind(self):
        values = self.count_values()
        return sorted(values.values()) == [1, 4]

    def full_house(self):
        values = self.count_values()
        return sorted(values.values()) == [2, 3]

    def flush(self):
        suits = [card.suit for card in self.hand]
        return len(set(suits)) == 1

    def straight(self):
        return (max(self.hand_ranks) - min(self.hand_ranks) == 4) and len(set(self.hand_ranks)) == 5
        # values = self.count_values()
        # rank_values = self.hand_ranks #[self.hand_ranks[i] for i in values]
        # value_range = max(rank_values) - min(rank_values)
        # if len(set(values.values())) == 1 and value_range == 4:
        #     return True
        # else:
        #     if set(values) == set("A 2 3 4 5".split()):
        #         return True
        #     else:
        #         return False

    def three_of_a_kind(self):
        values = self.count_values()
        return set(values.values()) == set([3, 1])

    def two_pairs(self):
        values = self.count_values()
        if sorted(values.values()) == [1, 2, 2]:
            self.hand_ranks = self.rank_values.get(max(values, key=values.get))
            return True

    def one_pair(self):
        values = self.count_values()
        if 2 in values.values():
            self.hand_ranks = self.rank_values.get(max(values, key=values.get))
            return True
    
    def high_card(self):
        values = self.count_values()
        self.hand_ranks = self.rank_values.get(max(values, key=values.get))
        return True


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
    player_1, player_2 = create_player_hands(hands)
    players = {
        "Player 1": player_1.find_best_hand(),
        "Player 2": player_2.find_best_hand()
        }
    print(players)
    winner = max(players, key=players.get)
    return winner
