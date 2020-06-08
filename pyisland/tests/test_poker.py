import pytest
import os
from src.classic_problems.poker import play

poker_examples = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources', 'poker.txt')
# with open(poker_examples, 'r') as f:
#     hands = f.readlines()

hands = [
    # By Pair of Eights
    ("5H 5C 6S 7S KD 2C 3S 8S 8D TD", "Player 2"),
    # By Highest Card Ace
    ("5D 8C 9S JS AC 2C 5C 7D 8S QH", "Player 1"),
    # By Flush with Diamonds
    ("2D 9C AS AH AC 3D 6D 7D TD QD", "Player 2"),
    # By Pair of Queens -> Highest Card Nine
    ("4D 6S 9H QH QC 3D 6D 7H QD QS", "Player 1"),
    # By Full House with 3 Fours
    ("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", "Player 1"),
    # By Royal Flush
    ("TS JS QS KS AS QH JH TH 9H 8H", "Player 1")
]

@pytest.mark.parametrize("hands, winner", hands)
def test_poker_game(hands, winner):
    result = play(hands)
    assert result == winner
