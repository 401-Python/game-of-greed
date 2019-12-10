import collections
import random
import math

class GameOfGreed():

    def __init__(self):
        pass

    def calculate_score(self, dice_roll):
        score = 0
        pairs = 0
        c = collections.Counter(dice_roll)

        '''handles mcflurry case'''
        if c[5] == 4 and c[1] == 2:
          print('A GRAND MCFLURRY')
          score += 2000
          return score

        '''Handles straights'''
        if 1 in c and 2 in c and 3 in c and 4 in c and 5 in c and 6 in c:
            score += 1500
            return score

        '''handles pairs'''
        for i in c:
            if c[i] == 2:
                pairs += 1
                if pairs == 3:
                    score = 0
                    score += 1500
                    return score

            '''handles fives, if there are fewer than 3'''
            if c[i] < 3 and i == 5:
                score += (c[i] * 50)

            '''handles ones, if there are fewer than 3'''
            if c[i] < 3 and i == 1:
                score += (c[i] * 100)

            '''handles trios of ones, and any leftover ones'''
            if c[i] >= 3 and i == 1:
                score += 1000
                c[i] -= 3
                for i in range(c[i]):
                    score += 1000
                continue
              
            '''handles trios of any roll other than one, and any leftovers'''
            if c[i] >= 3 and i != 1:
                score += (i * 100)
                c[i] -= 3
                for i in range(c[i]):
                    score += 100
                continue

        return score

    def greeting(self):
        print('Welcome to the Game of Greed!')

    def play_game(self):
        self.greeting()
        wanna_play = input('Wanna play? ')
        if wanna_play == 'y':
            print('Great! Check back tomorrow! :D')
        else:
            print('OK. Maybe another time')


if __name__ == "__main__":
    new_game = GameOfGreed()
    new_game.play_game()
