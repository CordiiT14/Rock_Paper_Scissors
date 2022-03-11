import unittest
from models.game import *
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Robbie", "rock")
        self.player2 = Player("Murphy", "scissors")
        self.player3 = Player("Charles", "paper")

        self.game = Game()

    
    def test_player_attribute_name(self):
        self.assertEqual("Robbie", self.player1.name)
    
    def test_player_attribute_choice(self):
        self.assertEqual("paper", self.player3.choice)

    def test_add_players_to_game(self):
        self.game.add_players(self.player1)
        self.assertEqual(1, len(self.game.players))
    
    def test_game_has_two_players(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        self.assertEqual(2, len(self.game.players))

    def test_two_players_only(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        self.game.add_players(self.player3)  
        self.assertEqual("Two players only", self.game.add_players(self.player3))
    
    def test_return_winner_rock(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        winner = Game.return_winner(self, self.game)
        self.assertEqual("Rock Wins!", winner)

    def test_return_winner_scissors(self):
        self.game.add_players(self.player2)
        self.game.add_players(self.player3)
        winner = Game.return_winner(self, self.game)
        self.assertEqual("Scissors Win!", winner)

    def test_return_winner_paper(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player3)
        winner = Game.return_winner(self, self.game)
        self.assertEqual("Paper Wins!", winner)
    
    def test_return_winner_none(self):
        self.game.add_players(self.player2)
        self.game.add_players(self.player2)
        winner = Game.return_winner(self, self.game)
        self.assertEqual( None , winner)