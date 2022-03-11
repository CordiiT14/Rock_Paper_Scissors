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
    
    def test_return_winner_rock_player1(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        winner = Game.return_winner(self, self.game)
        self.assertEqual("Player 1 wins by playing rock!", winner)
    
    def test_return_winner_rock_player2(self):
        self.game.add_players(self.player2)
        self.game.add_players(self.player1)
        winner = self.game.return_winner(self.game)
        self.assertEqual("Player 2 wins by playing rock!", winner)

    def test_return_winner_scissors_player1(self):
        self.game.add_players(self.player2)
        self.game.add_players(self.player3)
        winner = self.game.return_winner(self.game)
        self.assertEqual("Player 1 wins by playing scissors!", winner)

    def test_return_winner_scissors_player1(self):
        self.game.add_players(self.player3)
        self.game.add_players(self.player2)
        winner = self.game.return_winner(self.game)
        self.assertEqual("Player 2 wins by playing scissors!", winner)

    def test_return_winner_paper_player1(self):
        self.game.add_players(self.player3)
        self.game.add_players(self.player1)
        winner = self.game.return_winner(self.game)
        self.assertEqual("Player 1 wins by playing paper!", winner)

    def test_return_winner_paper_player2(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player3)
        winner = self.game.return_winner(self.game)
        self.assertEqual("Player 2 wins by playing paper!", winner)
    
    def test_return_winner_none(self):
        self.game.add_players(self.player2)
        self.game.add_players(self.player2)
        winner = self.game.return_winner(self.game)
        self.assertEqual( None , winner)