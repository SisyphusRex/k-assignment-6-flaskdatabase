"""pack validation test module"""

# System Imports
from unittest import TestCase

# First Party Imports
from views.utils import Utilities

# Third Party Imports


class PackValidationTest(TestCase):
    """validate pack test class"""

    def setUp(self):
        """set up method"""
        self.good_packs = ["750 ml", "24/16.9 oz", "20 lit bbl", "8 bottle package"]
        self.bad_packs = ["600ml"]
        self.utility = Utilities()

    def test_if_validates_good_packs(self):
        """iterates through list of good packs and validates"""

        # Arrange
        expected_return = True

        # Act

        # Assert
        for pack in self.good_packs:
            self.assertTrue(self.utility.is_valid_pack(pack))

    def test_if_invalidates_bad_packs(self):
        """iterates through bad packs and invalidates"""

        # arrange
        expected_return = False

        # act

        # assert
        for pack in self.bad_packs:
            self.assertFalse(self.utility.is_valid_pack(pack))
