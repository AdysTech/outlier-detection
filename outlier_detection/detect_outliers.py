import pandas as pd
import os
from .stsm import * 
import math

"""detects Level Shift outliers in a time series"""
class LevelShiftDetector:
    def __init__(self, timeseries):
        if not isinstance(timeseries, pd.DataFrame):
            raise TypeError('Must be DataFrame, but type was: {0}.'
                            .format(type(timeseries)))
        if not (isinstance(timeseries.index, pd.PeriodIndex) or
                isinstance(timeseries.index, pd.DatetimeIndex)):
            raise TypeError(
                'Must be DataFrame with DatetimeIndex or PeriodIndex.')
        if len(timeseries.columns) > 1:
            raise TypeError(
                'TimeSeriesModel currently understands only single value time series / dataframe')
        self._timeseries = timeseries

        def find_outliers(self):
            _stsm = TimeSeriesModel(self._timeseries)
            _stsm.FitTimeseries()
            n = len(self._timeseries)
            if n <= 50:
                self.critical_val = 3
            elif n >= 450:
                self.critical_val = 4
            else: 
                self.critical_val = round(3 + 0.0025 * (n - 50), 2)
        
        def _inner_loop(self):
            return