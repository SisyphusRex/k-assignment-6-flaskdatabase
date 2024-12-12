"""module to test Beverage model"""

# System Imports
from unittest import TestCase

# First Party imports
from models.beverage import Beverage

# Third Party Imports


class BeverageTest(TestCase):
    """class to test Beverage"""

    def setUp(self):
        self.id = "777777"
        self.name = "Test Drink"
        self.pack = "750 ml"
        self.price = "777.00"
        self.active = True
        self.test_beverage = Beverage(
            self.id, self.name, self.pack, self.price, self.active
        )

    def test_beverage_creation(self):
        """test beverage creation"""
        # Arrange
        expected_id = "777777"
        expected_name = "Test Drink"
        expected_pack = "750 ml"
        expected_price = "777.00"
        expected_active = True

        # act

        # Assert
        self.assertEqual(self.test_beverage.id, expected_id)
        self.assertEqual(self.test_beverage.name, expected_name)
        self.assertEqual(self.test_beverage.pack, expected_pack)
        self.assertEqual(self.test_beverage.price, expected_price)
        self.assertEqual(self.test_beverage.active, expected_active)
