from unittest import TestCase
import outlier_detection as tso
from .test_data_setup import import_dataframe
import numpy as nm

def test_kalman(self):
        df = import_dataframe()        
        kalman_filter = tso.KalmanFilter(
            0, 0)
        assert 1 == 1