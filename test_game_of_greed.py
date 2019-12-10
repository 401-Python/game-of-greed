from game_of_greed import GameOfGreed
import pytest

def test_non_scoring_roll():
  test_game = GameOfGreed()
  actual = test_game.calculate_score((2, 3, 4, 6, 3, 2))
  expected = 0
  assert actual == expected

def test_ones():
  test_game = GameOfGreed()
  actual = test_game.calculate_score((3, 1, 2, 1, 4, 4))
  expected = 200
  assert actual == expected

def test_twos():
  test_game = GameOfGreed()
  three_twos = test_game.calculate_score((2, 2, 2, 3, 4, 4))
  three_twos_score = 200

  five_twos = test_game.calculate_score((2, 2, 2, 3, 2, 2))
  five_twos_score = 400

  assert five_twos == five_twos_score
  assert three_twos == three_twos_score

def test_threes():
  test_game = GameOfGreed()
  three_threes = test_game.calculate_score((3, 3, 2, 3, 4, 4))
  three_threes_score = 300

  five_threes = test_game.calculate_score((3, 3, 3, 3, 3, 2))
  five_threes_score = 500

  assert five_threes == five_threes_score
  assert three_threes == three_threes_score

def test_fours():
  test_game = GameOfGreed()
  three_fours = test_game.calculate_score((4, 3, 2, 3, 4, 4))
  three_fours_score = 400

  five_fours = test_game.calculate_score((4, 4, 4, 4, 4, 2))
  five_fours_score = 600

  assert three_fours == three_fours_score
  assert five_fours == five_fours_score

def test_fives():
  test_game = GameOfGreed()
  three_fives = test_game.calculate_score((5, 3, 2, 3, 5, 5))
  three_fives_score = 500

  five_fives = test_game.calculate_score((5, 5, 5, 5, 5, 2))
  five_fives_score = 700

  two_fives = test_game.calculate_score((5, 2, 3, 4, 6, 5))
  two_fives_score = 100

  assert three_fives == three_fives_score
  assert five_fives == five_fives_score
  assert two_fives == two_fives_score

def test_sixes():
  test_game = GameOfGreed()
  three_sixes = test_game.calculate_score((6, 3, 2, 3, 6, 6))
  three_sixes_score = 600

  five_sixes = test_game.calculate_score((6, 6, 6, 6, 6, 2))
  five_sixes_score = 800

  assert three_sixes == three_sixes_score
  assert five_sixes == five_sixes_score

def test_straight():
  test_game = GameOfGreed()
  straight = test_game.calculate_score((4, 2, 6, 3, 1, 5))
  score = 1500
  assert straight == score

def test_three_pairs():
  test_game = GameOfGreed()
  three_pairs = test_game.calculate_score((1, 2, 3, 3, 2, 1))
  score = 1500
  assert three_pairs == score

def test_two_trios():
  test_game = GameOfGreed()
  two_trios_ones = test_game.calculate_score((1, 3, 1, 3, 1, 3))
  score_ones = 1300

  two_trios_normal = test_game.calculate_score((2, 4, 2, 4, 4, 2))
  score_normal = 600

  assert two_trios_normal == score_normal
  assert two_trios_ones == score_ones

def test_leftover_ones():
  test_game = GameOfGreed()
  leftovers = test_game.calculate_score((1, 1, 1, 4, 5, 1))
  score = 2050
  assert leftovers == score

def test_leftover_fives():
  test_game = GameOfGreed()
  leftovers = test_game.calculate_score((3, 3, 3, 4, 5, 4))
  score = 350
  assert leftovers == score

def test_grand_mcflurry():
  test_game = GameOfGreed()
  mcflurry = test_game.calculate_score((5, 5, 5, 5, 1, 1))
  score = 2000
  assert mcflurry == score