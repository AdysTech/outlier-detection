from unittest import TestCase
import outlier_detection as tso
from .test_data_setup import import_dataframe

class TestTimeSeriesModel(TestCase):

    def test_model(self):
        df = import_dataframe()
        _stsm = tso.TimeSeriesModel(df)
        print(df)

    def test_fit(self):
        df = import_dataframe()
        _stsm = tso.TimeSeriesModel(df)
        _stsm.FitTimeseries()
        print(df)