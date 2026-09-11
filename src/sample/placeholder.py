"""
A placeholder module for sample content
"""

from pathlib import Path
from random import randint

import sample

MODULE_DIR = Path(sample.__file__).resolve().parent
SQL_DIR = MODULE_DIR / "sql"


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

    def sample_3(self) -> str:
        """
        Sample method which returns the string contents of a sql file

        Returns
            sql query (str)
        """
        with open(SQL_DIR / "query1.sql", "r") as infile:
            return infile.read()
