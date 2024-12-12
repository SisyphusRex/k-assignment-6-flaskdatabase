"""module to test utils"""

# System Imports
from unittest import TestCase

# First Party Imports
from views.utils import Utilities

# Third Party Imports


class UtilsTest(TestCase):
    """utils test class"""

    def setUp(self):
        self.good_id = "777A6A"
        self.bad_id_not_6 = "gb3"
        self.bad_id_invalid_char = "762A8^"
        self.good_price = "75.00"
        self.bad_price = "AA.00"

        self.utility = Utilities()

    def test_id_validation(self):
        """test id validation"""

        # Arrange
        expected_good_id = True
        expected_not_6 = False
        expected_invalid_char = False

        # Act
        good_id_return = self.utility.is_valid_id(self.good_id)
        not_6_return = self.utility.is_valid_id(self.bad_id_not_6)
        invalid_char_return = self.utility.is_valid_id(self.bad_id_invalid_char)

        # Assert
        self.assertEqual(good_id_return, expected_good_id)
        self.assertEqual(not_6_return, expected_not_6)
        self.assertEqual(invalid_char_return, expected_invalid_char)

    def test_price_validation(self):
        """test price validation"""

        # Arrange
        expected_good_price = True
        expected_bad_price = False

        # Act
        good_price_return = self.utility.is_valid_price(self.good_price)
        bad_price_return = self.utility.is_valid_price(self.bad_price)

        # assert

        self.assertEqual(good_price_return, expected_good_price)
        self.assertEqual(bad_price_return, expected_bad_price)
