"""utility module"""


class Utilities:
    """utilities class"""

    # NOTE: I started this module to take the sort methods out of beverage.py, but I need to be able to pass
    # which attribute of Beverage to sort by
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
