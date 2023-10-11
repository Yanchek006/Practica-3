import unittest
from cities_game import CityGame


class TestCityGame(unittest.TestCase):

    def test_valid_city(self):
        game = CityGame()
        self.assertTrue(game.is_valid_city("Moscow"))

    def test_invalid_city(self):
        game = CityGame()
        self.assertFalse(game.is_valid_city("London_AXFDHGJH"))

    def test_add_city(self):
        game = CityGame()
        game.add_city("Moscow")
        self.assertIn("Moscow", game.cities)

    def test_check_city_exists(self):
        game = CityGame()
        game.add_city("Moscow")
        self.assertTrue(game.check_city_exists("Moscow"))

    def test_check_city_does_not_exist(self):
        game = CityGame()
        self.assertFalse(game.check_city_exists("Paris"))
