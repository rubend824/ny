"""
Classes for the FooBar exercise
"""


class Multiple:
    """
    This is a class that determines whether a number is
    a multiple of another or not
    """

    @staticmethod
    def is_multiple(number: int, multiple: int):
        """
        Determines whether a number is multiple of another or not

        Parameters:
           number (int): The incoming number to evaluate.
           multiple (int): The value of which number is or isn't a multiple.
        """
        return number % multiple == 0


class FooBar:
    """
    This is a class that evaluates an incoming the number.
    If the number is multiple of 3, it returns "Foo".
    For multiples of 5, it returns "Bar". And for numbers which are multiples
    of both 3 and 5, it returns "FooBar". In any other case, it returns the number
    itself.

    Attributes:
        _VALUES (list): The list of string values to print.
    """

    _VALUES = ['Foo', 'Bar', 'FooBar']

    def __init__(self, number: int = None):
        """
        The constructor for FooBar class. No initialization required

        Parameters:
           number (int): The incoming number to decide upon.
        """
        self.number = number

    def set_number(self, number):
        """
        Sets the number to evaluate

        Returns:
           number (int): The incoming number to decide upon.
        """
        self.number = number

    def get_printable_value(self):
        """
        The constructor for FooBar class. No initialization required

        Returns:
           printable_value (str): The printable value obtained.
        """
        printable_value = str(self.number)
        is_multiple_of_3 = Multiple.is_multiple(self.number, 3)
        is_multiple_of_5 = Multiple.is_multiple(self.number, 5)
        position = is_multiple_of_3 + is_multiple_of_5 * 2
        if bool(position):
            printable_value = self._VALUES[position - 1]
        return printable_value

