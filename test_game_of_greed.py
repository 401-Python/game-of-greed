from game_of_greed import Game
import pytest


@pytest.fixture
def game():
    return Game()


def test_zilch(game):
    expected = 0
    actual = game.calculate_score([])
    assert actual == expected


def test_ones(game):
    # (1) One
    expected = 100
    actual = game.calculate_score([3, 1])
    assert actual == expected

    # (2) Ones
    expected = 200
    actual = game.calculate_score([1, 2, 1])
    assert actual == expected

    # (3) Ones
    expected = 1000
    actual = game.calculate_score([1, 1, 4, 1])
    assert actual == expected

    # (4) Ones
    expected = 2000
    actual = game.calculate_score([3, 1, 1, 1, 1])
    assert actual == expected

    # (5) Ones
    expected = 3000
    actual = game.calculate_score([1, 2, 1, 1, 1, 1])
    assert actual == expected

    # (6) Ones
    expected = 4000
    actual = game.calculate_score([1, 1, 1, 1, 1, 1])
    assert actual == expected


def test_twos(game):
    # (1) Two
    expected = 0
    actual = game.calculate_score([2, 3])
    assert actual == expected

    # (2) Twos
    expected = 0
    actual = game.calculate_score([2, 2, 3])
    assert actual == expected

    # (3) Twos
    expected = 200
    actual = game.calculate_score([2, 2, 3, 2])
    assert actual == expected

    # (4) Twos
    expected = 400
    actual = game.calculate_score([2, 2, 3, 2, 2])
    assert actual == expected

    # (5) Twos
    expected = 600
    actual = game.calculate_score([2, 2, 3, 2, 2, 2])
    assert actual == expected

    # (6) Twos
    expected = 800
    actual = game.calculate_score([2, 2, 2, 2, 2, 2])
    assert actual == expected


def test_threes(game):
    # (1) Three
    expected = 0
    actual = game.calculate_score([2, 3])
    assert actual == expected

    # (2) Threes
    expected = 0
    actual = game.calculate_score([3, 2, 3])
    assert actual == expected

    # (3) Threes
    expected = 300
    actual = game.calculate_score([3, 3, 3, 2])
    assert actual == expected

    # (4) Threes
    expected = 600
    actual = game.calculate_score([3, 3, 3, 2, 3])
    assert actual == expected

    # (5) Threes
    expected = 900
    actual = game.calculate_score([3, 3, 3, 2, 3, 3])
    assert actual == expected

    # (6) Threes
    expected = 1200
    actual = game.calculate_score([3, 3, 3, 3, 3, 3])
    assert actual == expected


def test_fours(game):
    # (1) Four
    expected = 0
    actual = game.calculate_score([4, 3])
    assert actual == expected

    # (2) Fours
    expected = 0
    actual = game.calculate_score([4, 2, 4])
    assert actual == expected

    # (3) Fours
    expected = 400
    actual = game.calculate_score([4, 4, 4, 2])
    assert actual == expected

    # (4) Fours
    expected = 800
    actual = game.calculate_score([4, 4, 4, 2, 4])
    assert actual == expected

    # (5) Fours
    expected = 1200
    actual = game.calculate_score([4, 4, 4, 2, 4, 4])
    assert actual == expected

    # (6) Fours
    expected = 1600
    actual = game.calculate_score([4, 4, 4, 4, 4, 4])
    assert actual == expected


def test_fives(game):
    # (1) Five
    expected = 50
    actual = game.calculate_score([5, 3])
    assert actual == expected

    # (2) Fives
    expected = 100
    actual = game.calculate_score([5, 2, 5])
    assert actual == expected

    # (3) Fives
    expected = 500
    actual = game.calculate_score([5, 5, 5, 2])
    assert actual == expected

    # (4) Fives
    # Adjusted test so it doesn't cause a Grand McFlurry
    expected = 1000
    actual = game.calculate_score([5, 5, 5, 3, 5])
    assert actual == expected

    # (5) Fives
    expected = 1500
    actual = game.calculate_score([5, 5, 5, 2, 5, 5])
    assert actual == expected

    # (6) Fives
    expected = 2000
    actual = game.calculate_score([5, 5, 5, 5, 5, 5])
    assert actual == expected


def test_sixes(game):
    # (1) Six
    expected = 0
    actual = game.calculate_score([6, 3])
    assert actual == expected

    # (2) Sixes
    expected = 0
    actual = game.calculate_score([6, 2, 6])
    assert actual == expected

    # (3) Sixes
    expected = 600
    actual = game.calculate_score([6, 6, 6, 2])
    assert actual == expected

    # (4) Sixes
    expected = 1200
    actual = game.calculate_score([6, 6, 6, 2, 6])
    assert actual == expected

    # (5) Sixes
    expected = 1800
    actual = game.calculate_score([6, 6, 6, 2, 6, 6])
    assert actual == expected

    # (6) Sixes
    # changed from 3600
    expected = 2400
    actual = game.calculate_score([6, 6, 6, 6, 6, 6])
    assert actual == expected


def test_a_straight(game):
    expected = 1500
    actual = game.calculate_score([1, 2, 3, 4, 5, 6])
    assert actual == expected


def test_for_three_pairs(game):
    expected = 1500
    actual = game.calculate_score([1, 1, 2, 2, 3, 3])
    assert actual == expected


def test_for_leftover_ones(game):
    expected = 400
    actual = game.calculate_score([3, 3, 3, 1])
    assert actual == expected

    expected = 600
    actual = game.calculate_score([5, 5, 5, 1])
    assert actual == expected


def test_for_leftover_fives(game):
    expected = 1050
    actual = game.calculate_score([1, 1, 1, 5])
    assert actual == expected

    expected = 400
    actual = game.calculate_score([3, 3, 3, 5, 5])
    assert actual == expected


def test_for_two_trios(game):
    # 200 for 2s + 300 for 3s
    expected = 500
    actual = game.calculate_score([2, 2, 2, 3, 3, 3])
    assert actual == expected

    # 1000 for 1s + 400 for 4s
    # acual ==
    expected = 1400
    actual = game.calculate_score([1, 1, 1, 4, 4, 4])
    assert actual == expected


def test_roll_dice(game):
  actual = len(game.roll_dice(3))
  expected = 3
  assert actual == expected

  actual = len(game.roll_dice(4))
  expected = 4
  assert actual == expected

  actual = len(game.roll_dice(2))
  expected = 2
  assert actual == expected

  actual = len(game.roll_dice(0))
  expected = 0
  assert actual == expected


def test_pairs_ones_fives(game):
    actual = game.calculate_score((1, 1, 2, 2, 5, 5))
    assert actual == 1500


def test_final_round():
    flow = {
        'prints': [
            'Welcome to the Game of Greed!',
            'Game over! Your final score is 100',

        ],
        'prompts': [
            'Wanna play? Type y to roll ',
            'Would you like to keep 1? y for yes : n for no ',
            'Would you like to keep 2? y for yes : n for no ',
            'Would you like to keep 2? y for yes : n for no ',
            'Would you like to keep 3? y for yes : n for no ',
            'Would you like to keep 3? y for yes : n for no ',
            'Would you like to keep 4? y for yes : n for no ',
        
        ],
        'responses': [
            'y', 'y', 'y', 'y', 'y', 'y', 'y'
        ],
        'rolls': [
            [1, 2, 2, 3, 3, 4],
      
        ]
    }

    mp = MockPlayer(**flow)

    game = Game(mp.mock_print, mp.mock_input, 9)

    game.roll_dice = mp.mock_roll

    game.play_game()

    assert mp.mop_up()




class MockPlayer:
    def __init__(self, prints=[], prompts=[], responses=[], rolls=[]):
        self.prints = prints
        self.prompts = prompts
        self.responses = responses
        self.rolls = rolls

    def mock_print(self, *args):
        if len(self.prints):
            current_print = self.prints.pop(0)
            assert args[0] == current_print

    def mock_input(self, *args):
        if len(self.prompts):
            current_prompt = self.prompts.pop(0)
            assert args[0] == current_prompt

        if len(self.responses):
            current_response = self.responses.pop(0)
            return current_response

    def mock_roll(self, num_dice):
        if len(self.rolls):
            current_roll = self.rolls.pop(0)
            return current_roll

    def mop_up(self):
        assert len(self.prints) == 0
        assert len(self.prompts) == 0
        assert len(self.responses) == 0
        assert len(self.rolls) == 0
        return True
