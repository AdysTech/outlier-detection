import outlier_detection as tso
from .test_data_setup import import_dataframe
import numpy as nm


class TestLSOutlier:

    def test_init(self):
        df = import_dataframe()
        ls = tso.LevelShiftDetector(df)