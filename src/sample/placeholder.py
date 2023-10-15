"""
A placeholder module for sample content
"""
from random import randint


class Sample:
    """
    Sample class required to setup unittests and other checks
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sample_0(self) -> None:
        """
        Sample method that does nothing
        """
        return None

    def sample_1(self) -> str:
        """
        Sample method which returns the class name

        Returns:
            class name (str): str representation of class name
        """
        return self.__class__.__name__

    def sample_2(self, x: int) -> int:
        """
        Sample method which returns a random int between 0 and x

        Args:
            x (int): outer bound from zero

        Returns
            random int (int)
        """
        return randint(min(0, x), max(0, x))
