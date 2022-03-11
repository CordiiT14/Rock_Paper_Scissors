import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Robbie", "rock")
        self.player2 = Player("Murphy", "scissors")
        self.player3 = Player("Charles", "paper")

    
    def test_player_attribute_name(self):
        self.assertEqual("Robbie", self.player1.name)
    
    def test_player_attribute_choice(self):
        self.assertEqual("paper", self.player3.choice)

    def test_add_players_to_game(self):
        game = Game(self.player1, self.player2)
        self.assertEqual(2, len(game.players))
    