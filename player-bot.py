from game_of_greed import Game


class Player:
    def __init__(self):
        pass

    def _print(self, *args):
        print('bot')
        print(args)

    def _input(self, *args):
        print('bot')
        return input(args)



if __name__ == "__main__":
    bot = Player()
    game = Game(bot._print, bot._input)
    game.play_game()
