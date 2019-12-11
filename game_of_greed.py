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
                multiplyer = i
                score += (i * 100)
                leftovers = c[i] - 3
                while leftovers > 0:
                    print('m', multiplyer)
                    print('c', leftovers)
                    score += (multiplyer * 100)
                    leftovers -=1
                continue

        return score

    def greeting(self):
        print('Welcome to the Game of Greed!')

    def play_game(self):
        self.greeting()
        wanna_play = input('Wanna play? Type y to roll')
        if wanna_play == 'y':
            self.choose_keepers(self.roll_dice(self.available_dice))
        else:
            print('OK. Maybe another time')

    def roll_dice(self, available_dice):

        '''
        This method generates a dice roll using the available_dice state. 
        It generates up to 6 random numbers between 1 and 6, and returns a tuple of those numbers. 
        If the roll would result in a score of zero, we reset the bank, available dice, and increment the round
        '''
        if not available_dice:
          available_dice = self.available_dice
        dice = []
        if available_dice == 0:
            return ()
        for i in range(available_dice):
            dice.append(random.randint(1, 6))
            roll = tuple(dice)
        print('You rolled ' + str(roll))
       
        return roll

    def choose_keepers(self, dice_roll):
        '''
        This method accepts a tuple and allows the user to select which dice to add to their score.
        We begin by iterating through the tuple, and prompting the user for an input of y or n.
        If the user responds with y, the corresponding dice is added to a list.
        After we've gone through the entire tuple, we take our list of keepers and
        pass it into our calculate score function, bank it, then the roll_again func
        '''
        keepers = []

        for dice in dice_roll:
            pickem = input(
                f'Would you like to keep {dice}? y for yes : n for no ')
            if pickem == 'y':
                keepers.append(dice)
                self.available_dice -= 1
        score = self.calculate_score(tuple(keepers))
        self.bank += score
        self.roll_again()

        return tuple(keepers)

    def roll_again(self):
        '''This function lets the user continue rolling for a higher score.
        It first checks if the user still has any dice remaining, if they do, they're prompted
        to roll again, if they choose y, we roll and make sure it's a scoring roll.
        If it's not a scoring roll, their bank is reset to 0 and the next round starts.
        If it is a scoring roll, they get to choose keepers again.
        If they elect not to roll again, whatever is in their bank is added to the total score
        and we call the start_next_round function
        '''
        if self.available_dice > 0:
            roll_again = input(
                f'You have {self.bank} points ready to bank, and {self.available_dice} dice remaining. Would you like to risk them and roll again? ')
            if roll_again == 'y':
                roll = self.roll_dice()
                gamble = self.calculate_score(roll)
                if gamble == 0:
                    self.bank == 0
                    print('Sorry, you just lost everything!')
                    self.start_next_round()

                else:
                    print(
                        f'Greed paid off!')
                    self.choose_keepers(roll)

            elif roll_again == 'n':
                print(
                    f'Smart move, take the money and run! {self.bank} points added to your total')
                self.total_score += self.bank
                self.start_next_round()

        elif self.available_dice == 0:
            self.total_score += self.bank
            self.start_next_round()

    def show_score(self):
        print(f'your current score is {self.total_score}')

    def start_next_round(self):
        '''This function increments essentially sets the state for the next round by
        incrementing the current round, resetting the bank to 0 and available_dice to 6.
        Total_score is maintained throughout the game until the end
        '''
        self.current_round += 1
        print(
            f'Get ready for round {self.current_round}! Current score: {self.total_score}')
        self.bank = 0
        self.available_dice = 6
        self.choose_keepers(self.roll_dice())


if __name__ == "__main__":
    new_game = Game()
    new_game.play_game()
