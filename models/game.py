import random
from models.player import Player

class Game():
    def __init__(self):
        self.players = []

    def add_players(self, player):
        if len(self.players) < 2:
            self.players.append(player)
            return
        else:
            return "Two players only"

    
    def return_winner(self, game):
        choices_played = [game.players[0].choice, game.players[1].choice]
        if "rock" in choices_played and "scissors" in choices_played:
            # return '/rock/scissors'
            return 'rock'
        if "scissors" in choices_played and "paper" in choices_played:
            # return '/scissors/rock'
            return 'scissors'
        if "paper" in choices_played and "rock" in choices_played:
            # return '/paper/rock'
            return 'paper'
        else:
            return

    def display_winner(self, player1, winning_choice):
        if player1.choice == winning_choice:
            return 'Player 1'
        else:
            return 'Player 2'

    def computer_player(self):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        computer_player = Player('Computer', computer_choice)
        return computer_player 
