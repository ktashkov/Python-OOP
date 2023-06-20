from project.tennis_player import TennisPlayer
import unittest

class TestTennisPlayer(unittest.TestCase):

    def test_constructor(self):
        player = TennisPlayer("Roger Federer", 39, 9500)
        self.assertEqual(player.name, "Roger Federer")
        self.assertEqual(player.age, 39)
        self.assertEqual(player.points, 9500)
        self.assertEqual(player.wins, [])

    def test_name_setter(self):
        with self.assertRaises(ValueError):
            TennisPlayer("RF", 39, 9500)

    def test_age_setter(self):
        with self.assertRaises(ValueError):
            TennisPlayer("Roger Federer", 17, 9500)

    def test_add_new_win(self):
        player = TennisPlayer("Roger Federer", 39, 9500)
        self.assertEqual(player.add_new_win("Wimbledon"), None)
        self.assertEqual(player.add_new_win("Wimbledon"), "Wimbledon has been already added to the list of wins!")
        self.assertEqual(player.wins, ["Wimbledon"])

    def test_lt(self):
        player1 = TennisPlayer("Roger Federer", 39, 9500)
        player2 = TennisPlayer("Novak Djokovic", 34, 11000)
        self.assertEqual(player1 < player2,
                         "Novak Djokovic is a top seeded player and he/she is better than Roger Federer")

    def test_str(self):
        player = TennisPlayer("Roger Federer", 39, 9500)
        player.add_new_win("Wimbledon")
        player.add_new_win("Australian Open")
        expected_output = "Tennis Player: Roger Federer\nAge: 39\nPoints: 9500.0\nTournaments won: Wimbledon, Australian Open"
        self.assertEqual(str(player), expected_output)


if __name__ == '__main__':
    unittest.main()
