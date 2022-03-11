from random import choices
from models.player import Player

class Game():
    def __init__(self, player1, player2):
        self.players = [player1, player2]


    def return_winner(players):
        choices_played = [players[0].choice.lower(), players[1].choice.lower()]
        if "rock" in choices_played and "scissors" in choices_played:
            return "Rock Wins!"
        if "scissors" in choices_played and "paper" in choices_played:
            return "Scissors Win!"
        if "paper" in choices_played and "rock" in choices_played:
            return "Paper Wins!"
        else:
            return
        