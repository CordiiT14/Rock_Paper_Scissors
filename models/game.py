from random import choices
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
            return '/rock/scissors'
        if "scissors" in choices_played and "paper" in choices_played:
            return '/scissors/rock'
        if "paper" in choices_played and "rock" in choices_played:
            return '/paper/rock'
        else:
            return

    # def display_winner(self, player1, winning_choice):
    #     if player1.choice == winning_choice:
    #         return 'Player 1'
    #     else:
    #         return 'Player 2'