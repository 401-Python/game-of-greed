import pytest
from game import Game


@pytest.fixture()
def game():
    return Game()

@pytest.mark.parametrize("roll, keepers, expected",[
    ([1,2,3],(1,),True),
    ([1,2,3],(1,2),True),
    ([1,2,3],(1,2,3),True),
    ([1,2,3],(6,),False),
    ([1,2,3],(1,1),False),
])
def test_validate(game, roll, keepers, expected):
    actual = game.validate(roll, keepers)
    assert actual == expected

@pytest.mark.parametrize("roll,expected_keepers",[([1,2,3],(1,)),([4,5,6],(5,6))])
def test_def_validate_roll_success(roll, expected_keepers):

    def my_print(msg, *args):
        assert msg == roll

    def my_input(msg, *args):
        assert msg == 'Enter dice to keep: '
        keeper_string = ''
        for val in expected_keepers:
            keeper_string += str(val)

        return keeper_string

    game = Game(my_print, my_input)

    keepers = game.validate_roll(roll)

    assert keepers == expected_keepers

@pytest.mark.parametrize("roll,expected_keepers",[
    ([1,2,3],(1,)),
    ([4,5,6],(6,)),
])
def test_def_validate_roll_fail(roll, expected_keepers):

    prints = ['No way pal', roll, 'No way pal',roll]

    inputs = ['0','0', str(expected_keepers[0])]

    def my_print(msg, *args):
        assert msg == prints.pop(0)

    def my_input(msg, *args):
        assert msg == 'Enter dice to keep: '
        return inputs.pop(0)

    game = Game(my_print, my_input)

    keepers = game.validate_roll(roll)

    assert keepers == expected_keepers


