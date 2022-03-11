from random import choices
from models.player import Player

class Game():
    def __init__(self, ):
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
            if game.players[0].choice == "rock":
                return "Player 1 wins by playing rock!"
            else:
                return 'Player 2 wins by playing rock!'
        if "scissors" in choices_played and "paper" in choices_played:
            if game.players[0].choice == "scissors":
                return "Player 1 wins by playing scissors!"
            else:
                return "Player 2 wins by playing scissors!"
        if "paper" in choices_played and "rock" in choices_played:
            if game.players[0].choice == "paper":
                return "Player 1 wins by playing paper!"
            else:
                return "Player 2 wins by playing paper!"
        else:
            return
        