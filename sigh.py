import collections
import random
import math


class GameOfGreed():
    available_dice = 6
    current_round = 1
    bank = 0
    total_score = 0

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

        '''Handles straights, if the counter length is 6
        it means there's one of each dice roll'''
        if len(c) == 6:
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
        wanna_play = input('Wanna play? Type y to roll')
        if wanna_play == 'y':
            self.choose_keepers(self.roll_dice())
        else:
            print('OK. Maybe another time')

    def roll_dice(self):
        dice = []
        for i in range(self.available_dice):
            dice.append(random.randint(1, 6))
            roll = tuple(dice)
        if self.calculate_score(roll) == 0:
            print('Too greedy! You lost everything :D')
            self.bank = 0
            self.current_round += 1
            self.available_dice = 0
            return ()
        print('You rolled ' + str(roll))
        return roll

    def choose_keepers(self, dice_roll):
        keepers = []
        for dice in dice_roll:
          pickem = input(
              f'Would you like to keep {dice}? Y for yes : N for no ')
          if pickem == 'Y':
              keepers.append(dice)
              self.available_dice -= 1
          if self.available_dice == 0:
            self.current_round += 1
            score = self.calculate_score(tuple(keepers))
            self.total_score += score
            print(
                f'Total score to start round {self.current_round}: {self.total_score}')

        self.roll_again()

        return tuple(keepers)

    def roll_again(self):
        if self.available_dice > 0:
            roll_again = input(
                f'You have {self.bank} points ready to bank, and {self.available_dice} dice remaining. Would you like to risk them and roll again? ')
            if roll_again == 'Y':
                self.choose_keepers(self.roll_dice())
                # gamble = self.calculate_score(self.roll_dice())
                # if gamble == 0:
                #     self.bank == 0
                #     print('Sorry, you just lost everything!')
                #     self.current_round +=1
                #     return
            elif roll_again == 'N':
                print(
                    f'Smart move, take the money and run! {self.bank} points added to your total')
                self.total_score += self.bank
                return

    def show_score(self):
        print(f'your current score is {self.total_score}')


if __name__ == "__main__":
    new_game = GameOfGreed()
    new_game.play_game()

















import collections
import random
import math


class Game():
    available_dice = 6
    current_round = 1
    bank = 0
    total_score = 0

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

        '''Handles straights, if the counter length is 6
        it means there's one of each dice roll'''
        if len(c) == 6:
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
        wanna_play = input('Wanna play? Type y to roll')
        if wanna_play == 'y':
            self.choose_keepers(self.roll_dice())
        else:
            print('OK. Maybe another time')

    def roll_dice(self):
        dice = []
        for i in range(self.available_dice):
            dice.append(random.randint(1, 6))
            roll = tuple(dice)
        print('You rolled ' + str(roll))
        if self.available_dice == 0:
          return ()
        return roll

    def choose_keepers(self, dice_roll):
        keepers = []

        for dice in dice_roll:
            pickem = input(
                f'Would you like to keep {dice}? y for yes : n for no ')
            if pickem == 'Y':
                keepers.append(dice)
                self.available_dice -= 1
        score = self.calculate_score(tuple(keepers))
        self.bank += score
        self.roll_again()

        return tuple(keepers)

    def roll_again(self):
        roll_again = input(
            f'You have {self.bank} points banked, and {self.available_dice} dice remaining. Would you like to risk them and roll again? ')
        if roll_again == 'Y':
            roll = self.roll_dice()
            gamble = self.calculate_score(roll)
            if gamble == 0:
                self.bank == 0
                print('Sorry, you just lost everything!')
                return
            else:
                self.total_score += (gamble + self.bank)
                print(
                    f'Greed paid off!')
                self.choose_keepers(roll)
                self.current_round +=1
                self.available_dice = 0
        elif roll_again == 'N':
          print(f'Smart move, take the money and run! {self.bank} points added to your total')
          self.total_score += self.bank
    
    def show_score(self):
      print(f'your current score is {self.total_score}')

if __name__ == "__main__":
    new_game = Game()
    new_game.play_game()
