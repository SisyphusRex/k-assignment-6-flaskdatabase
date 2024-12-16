"""utility module"""


class Utilities:
    """utilities class"""

    def is_valid_id(self, input_string: str) -> bool:
        """validate whether ID is 5 characters and only includes alphabet and numbers"""
        if len(input_string) != 5:
            return False
        valid_chars = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "X",
            "W",
            "Z",
        ]
        for char in input_string:
            if char not in valid_chars:
                return False
        return True

    def is_valid_pack(self, input_string: str) -> bool:
        """validate pack"""
        # NOTE: this validation is close but not quite correct.  Some existing beverages have no space in the string
        # and thus cannot be split.
        split_string = input_string.split()
        if len(split_string) == 1:
            return False
        for char in split_string[0]:
            try:
                my_int = int(char)
                return True
            except ValueError:
                pass
        return False

    def is_valid_price(self, input_string: str) -> bool:
        """validate if price is a float"""
        try:
            price = float(input_string)
        except ValueError:
            return False
        return True

    # NOTE: I started this module to take the sort methods out of beverage.py, but I need to be able to pass
    # which attribute of Beverage to sort by

    # NOTE: I would have to use a lambda function to pass the key (beverage attribute) to the method
    def sort_ascending(self, my_collection: list) -> None:
        """method to sort ascending using bubble sort"""
        for index in range(len(my_collection)):
            for index2 in range(len(my_collection)):
                if my_collection[index].pack < my_collection[index2].pack:
                    temp = my_collection[index]
                    my_collection[index] = my_collection[index2]
                    my_collection[index2] = temp

    def sort_descending(self, my_collection: list) -> None:
        """sort in descending order using bubble sort"""
        for index in range(len(my_collection)):
            for index2 in range(len(my_collection)):
                if my_collection[index].pack > my_collection[index2].pack:
                    temp = my_collection[index]
                    my_collection[index] = my_collection[index2]
                    my_collection[index2] = temp
