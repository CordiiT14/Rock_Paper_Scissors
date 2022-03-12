import random

class Player():
    def __init__(self, player_name, choice):
        self.name = player_name
        self.choice = choice 

    # def computer_player(self):
    #     choices = ['rock', 'paper', 'scissors']
    #     choice = random.choices(choices)
    #     computer_player = Player('Computer', choice)
    #     return computer_player 