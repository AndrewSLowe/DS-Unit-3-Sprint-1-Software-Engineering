"""
Classes to represent games
"""
# Need imports!
from random import random

# Always start with a capital letter. Lower cases are an instance of the class
# Pass is a null value==>Doesn't do anything. Classes have to end in pass.

# class Game:
    # pass

# A variable declared inside of a class is called a field
class Game:
    #This is a dog string
    """
    General representation of an abstract game
    """
    fun_level = 5

    def __init__(self, rounds=2, player1 = 'owen', player2 = 'jean'):
        self.rounds = rounds
        self.steps = 5
        self.player1 = player1
        self.player2 = player2
    # Function inside a class is called a method.
    # __init__ is a special function called a constructor

    def print_players(self):
        """
        Print players
        """
        prunt('{} is playing {}.format(self.player1,self.player2')

    def add_round(self):
        """
        increment number of rounds
        """
        self.rounds += 1

    def winner(self):
        """randomly picka  and return winner"""
        return self.player1 if random() > 0.5 else self.player2

class Tic(Game):
    """subclass of Game called Tictactoe"""

    def __init__(self, rounds=3, player1 = 'Riley', player2='Amer'):
        super().__init__(rounds, player1, player2)     #Have to override older init with super

    def print_players(self):
        print('{} is playing TicTacToe with {}'.format(self.player1,self.player2))
