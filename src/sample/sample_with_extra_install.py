"""
A placeholder module for sample content requiring the "df" extra install
"""

try:
    import pandas as pd
except ImportError:
    pass

from sample.placeholder import Sample


class SampleWithExtraInstall(Sample):
    """
    Sample class requiring the "df" extra install
    """

    def sample_extra(self):
        """
        Sample method which returns an empty pandas DataFrame

        Returns:
            df (pandas.DataFrame): empty DataFrame
        """
        df = pd.DataFrame()
        return df
