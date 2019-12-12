import pytest
from game import Game
import game

def test_module_doc():
    assert game.__doc__ != None

@pytest.mark.parametrize("num_dice",[1,2,3,4,5,6])
def test_roll(num_dice):
    game = Game()
    roll = game._do_roll(num_dice)
    assert len(roll) == num_dice
    for val in roll:
        assert 1 <= val <= 6

