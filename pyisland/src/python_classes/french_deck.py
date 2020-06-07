from collections import namedtuple
from collections.abc import MutableSequence
from random import shuffle

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value
    
    def __delitem__(self, position):
        del self._cards[position]
    
    def insert(self, position, value):
        self._cards.insert(position, value)
    
    def shuffle_deck(self):
        return shuffle(self._cards)
    
    def get_rank(self, rank):
        return [card for card in self._cards if card.rank == str(rank).upper()]
    
    def get_suit(self, suit):
        return [card for card in self._cards if card.suit == suit]
    
    def get_royal(self, suit):
        return [card for card in self._cards if card.suit == suit and card.rank not in [str(n) for n in range(2, 10)]]


class Hand:
    def __init__(self, hand=None):
        self.deck = FrenchDeck()
        self.deck.shuffle_deck()
        self.hand = hand
    
    def __len__(self):
        return len(self.hand)

    def draw(self, size):
        cards = [self.deck.pop(i) for i in range(size)]
        self.hand = cards
    
    def draw_from_rank(self, rank, size=4):
        cards = [self.deck.get_rank(rank).pop(i) for i in range(size)]
        self.hand = cards
    
    def draw_from_suit(self, suit, size=4):
        cards = [self.deck.get_suit(suit).pop(i) for i in range(size)]
        self.hand = cards
    
    def draw_from_royal(self, suit, size=5):
        cards = [self.deck.get_royal(suit).pop(i) for i in range(size)]
        self.hand = cards
