import pytest
import os
from src.classic_problems.poker import Card, Poker, create_player_hands, play

poker_examples = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources', 'poker.txt')


with open(poker_examples, 'r') as f:
    hands = f.readlines()

class TestPokerInitialValues:
    player = Poker(hands[0].split()[:5])

    def test_poker_str(self):
        assert isinstance(str(self.player), str)
    
    def test_poker_hand(self):
        assert isinstance(self.player.hand, list)

    def test_poker_ranks(self):
        expected_ranks = [str(n) for n in range(2, 10)] + list("TJQKA")
        assert self.player.ranks == expected_ranks

    # def test_card_value_order(self):
    #     expected_rank_value_order = {rank: value+2 for value, rank in enumerate(self.player.ranks)}
    #     assert self.player.rank_value_order == expected_rank_value_order


@pytest.mark.parametrize('hands', hands)
def test_poker_hands_are_split(hands):
    player_1, player_2 = create_player_hands(hands)
    assert len(player_1.hand) == 5
    assert len(player_2.hand) == 5

@pytest.mark.parametrize('hands', hands)
def test_poker_hands_are_parsed_into_card_objects(hands):
    player_1, player_2 = create_player_hands(hands)
    def check_card_instances(hand):
        for card in hand:
            assert isinstance(card, Card)
            assert isinstance(card.rank, str)
            assert isinstance(card.suit, str)
            assert card.rank in player_1.ranks
            assert card.suit in list("SHCD")
    
    check_card_instances(player_1.hand)
    check_card_instances(player_2.hand)

@pytest.mark.parametrize('hands', hands)
def test_winning_poker_hand(hands):
    result = play(hands)
    print(hands[0])
