try:
    import pandas as pd
except ImportError:
    pass

from sample.placeholder import Sample


class SampleWithExtraInstall(Sample):
    def sample_extra(self):
        df = pd.DataFrame()
        return df
