class Player(object):
    """ Player Class which contains all the necessary tracking attributes"""
    def __init__(self, name="Player"):
        """ Initializes Player name, initial token count of 1000, and number of plays, wins and losses as 0 at
        the start of the game, along with a simple welcome message."""
        self.player_name = name
        self.__token = 1000
        self.num_of_plays = 0
        self.__wins = 0
        self.__losses = 0
        print(f"\nHey, {self.player_name}! Welcome to Jacob Kustra's blackjack game. "
              f"You will start with $1000 in tokens.")

    def token_count(self):
        """ Returns the player's current token count. """
        return self.__token

    def token_win(self, bet_amount):
        """ Adds the amount of tokens the player bet if they win. """
        token_amount = self.token_count()
        self.__token = token_amount + bet_amount

    def token_loss(self, bet_amount):
        """ Subtracts the amount of tokens the player bet if they lose. """
        token_amount = self.token_count()
        self.__token = token_amount - bet_amount

    def play_count(self):
        """ Returns the current number of rounds played. """
        return self.num_of_plays

    def add_round(self):
        """ Adds one round to the current number of rounds played. """
        rounds = self.play_count()
        self.num_of_plays = rounds + 1

    def win_count(self):
        """ Returns the current number of rounds the player has won. """
        return self.__wins

    def add_win(self):
        """ Adds one win to the current number of rounds the player has won. """
        self.__wins = self.win_count() + 1
        return self.__wins

    def loss_count(self):
        """ Returns the current number of rounds the player has lost. """
        return self.__losses

    def add_loss(self):
        """ Adds one loss to the current number of rounds the player has lost. """
        self.__losses = self.loss_count() + 1
        return self.__losses

    def __win_loss_ratio_calc(self, wins=0, losses=0):
        """ Calculates and returns the players win loss ratio account for if they have 0 losses as to
        avoid dividing by zero. """
        if losses == 0:
            if wins == 0:
                self.__win_loss_ratio = 0.0
            else:
                self.__win_loss_ratio = 1.0
        else:
            self.__win_loss_ratio = (wins / losses)
        return self.__win_loss_ratio

    def __win_percentage(self, wins=0):
        """ Calculates and returns the players win percentage based off of the total number of rounds
        they have played. """
        self.__win_perc = (wins / self.play_count()) * 100
        return self.__win_perc

    def __call__(self):
        """ Prints out a reminder for the player to take they voucher which is generated. """
        print(f"\n** Remember to take your voucher file containing {self.token_count()} tokens. **"
              f"\n-----------------------------------------------------------")

    def __str__(self):
        """ Prints out the final thank message thanking the player for playing and summarizing their stats. """
        string0 = "\n-----------------------------------------------------------"
        string1 = f"\nThanks for playing, {self.player_name}. You finished with {self.token_count()} tokens." \
                  f"\nNumber of rounds played: {self.play_count()}"
        string2 = "\nWin/loss ratio: {:,.2f}".format(self.__win_loss_ratio_calc(self.win_count(), self.loss_count())) \
                  + "\nWin Percentage: {:,.2f}%".format(self.__win_percentage(self.win_count()))
        return string0 + string1 + string2
