from collections import defaultdict
from random import choice
from .french_deck import FrenchDeck, Hand


class Poker:
    """ Find a winning Poker hand. """

    def __init__(self, hand):
        self.hand = hand
        self.card_order_dict = {str(k): k for k in range(2, 11)}
        self.card_order_dict.update({
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        })
    
    def count_values(self):
        values = [card.rank for card in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        return value_counts

    def get_winning_hand(self):
        if self.check_royal_flush():
            return {"Royal flush": 10}
        if self.check_straight_flush():
            return {"Straight flush": 9}
        if self.check_four_of_a_kind():
            return {"Four of a kind": 8}
        if self.check_full_house():
            return {"Full house": 7}
        if self.check_flush():
            return {"Flush": 6}
        if self.check_straight():
            return {"Straight": 5}
        if self.check_three_of_a_kind():
            return {"Three of a kind": 4}
        if self.check_two_pairs():
            return {"Two pairs": 3}
        if self.check_one_pair():
            return {"One pair": 2}
        return {"High card": 1}

    def check_royal_flush(self):
        ranks = [card for card in self.hand if card.rank not in [str(n) for n in range(2, 10)]]
        return True if len(ranks) == 5 and self.check_straight_flush() else False

    def check_straight_flush(self):
        return True if self.check_flush() and self.check_straight() else False

    def check_four_of_a_kind(self):
        values = self.count_values()
        return True if sorted(values.values()) == [1, 4] else False

    def check_full_house(self):
        values = self.count_values()
        return True if sorted(values.values()) == [2, 3] else False

    def check_flush(self):
        suits = [card.suit for card in self.hand]
        return True if len(set(suits)) == 1 else False

    def check_straight(self):
        values = self.count_values()
        rank_values = [self.card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(values.values())) == 1 and value_range == 4:
            return True
        else:
            if set(values) == set("A 2 3 4 5".split()):
                return True
            else:
                return False

    def check_three_of_a_kind(self):
        values = self.count_values()
        return True if set(values.values()) == set([3, 1]) else False

    def check_two_pairs(self):
        values = self.count_values()
        return True if sorted(values.values()) == [1, 2, 2] else False

    def check_one_pair(self):
        values = self.count_values()
        return True if 2 in values.values() else False


if __name__ == "__main__":
    hand = Hand()
    hand.draw_from_royal('hearts', 5)
    print(hand.hand)
    poker_hand = Poker(hand.hand)
    print(poker_hand.get_winning_hand())
