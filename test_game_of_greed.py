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
