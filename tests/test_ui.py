from unittest import TestCase
from unittest.mock import patch
import ui


class TestUi(TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_get_price_with_number(self, mock_input):
        self.assertEqual(3, ui.get_price())

    @patch('builtins.input', side_effect=['a', '-3', '1000000000', '3 3', '3'])
    def test_get_price_with_bad_inputs(self, mock_input):
        self.assertEqual(3, ui.get_price())

    @patch('builtins.input', side_effect=['', 'some name'])
    def test_get_string_rejects_empty_inputs(self, mock_input):
        question = "Please enter a name:"
        self.assertEqual('some name', ui.get_string(question))