import pytest

from game import Game

def test_straight():
    game = Game()
    actual = game.calculate_score((3,2,4,5,1,6))
    expected = 1500
    assert actual == expected

def test_3_pairs():
    game = Game()
    actual = game.calculate_score((3,2,4,3,2,4))
    expected = 1500
    assert actual == expected
