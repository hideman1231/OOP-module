from unittest import TestCase
from unittest.mock import patch, mock_open

from models import Player


class TestEnemy(TestCase):

    @patch('models.Enemy.select_attack', return_value=1)
    def test_select_attack(self, select_attack):
        self.assertEqual(select_attack(), 1)


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('test', 1, 1, 1)

    def test_fight(self):
        self.assertEqual(self.player.fight(1, 1), 0)
        self.assertEqual(self.player.fight(1, 3), -1)
        self.assertEqual(self.player.fight(3, 1), 1)

    def test_validate_names(self):
        self.assertIsNone(self.player.validate_names(self.player.name))

    def test_validate_names_mock(self):
        with patch('builtins.open', mock_open(read_data='name')):
            self.assertIsNone(self.player.validate_names(self.player.name))

    def test_validate_allowed_attacks(self):
        self.assertIsNone(self.player.validate_allowed_attacks())
