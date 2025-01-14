try:
    import pandas as pd
except ImportError:
    pass
import pytest

from sample.sample_with_extra_install import SampleWithExtraInstall


@pytest.mark.df
class TestSampleWithExtraInstall:
    def test_sample_extra(self):
        # Arrange
        sample = SampleWithExtraInstall()
        # Act
        result = sample.sample_extra()
        # Assert
        assert isinstance(result, pd.DataFrame)
        assert result.empty
