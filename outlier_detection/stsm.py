import pandas as pd
import os
import numpy as nm

"""Fit the basic structural time series model by maximum likelihood"""


class TimeSeriesModel:

    """generates local level model (random walk plus noise) for the passed in time series DataFrame."""

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
        # if len(timeseries.applymap(lambda x: isinstance(x, (int, float))).all(0)) > 0:
        #     raise TypeError(
        #         'TimeSeriesModel currently understands only numerical columns of a dataframe')
        self._constant_matrix = None
        self._spectral_matrix = None
        self._scaled_variance = None
        self._spectral_density = None
        self._spectral_matrix = None
        self._constant_matrix = None
        self._timeseries = timeseries
        self._model()

    @property
    def spectral_matrix(self):
        """matrix created based on half angles of incoming timeseries"""
        return self._spectral_matrix

    @property
    def successive_differences(self):
        """successive differences"""
        return self._timeseries.diff()

    @property
    def scaled_variance(self):
        """scaled variance 1e6 is scaling factor"""
        return self._scaled_variance

    @property
    def spectral_density(self):
        """discrete Fourier Transformed time series"""
        return self._spectral_density

    @property
    def series_mean(self):
        """discrete Fourier Transformed time series"""
        return self._series_mean

    @property
    def constant_matrix(self):
        """matrix calculated based on half angles"""
        return self._constant_matrix

    def _model(self):
        self._scaled_variance = 1e6 * (self._timeseries.var(skipna=True) / 100)
        self._series_mean = self._timeseries.mean(
            skipna=True, numeric_only=True)
        first_value = self._timeseries.loc[[
            self._timeseries.first_valid_index()]].values.item(0)
        self._spectral_density = pd.DataFrame(data=nm.fft.fft(self.successive_differences)**2 /
                                              (2 * nm.pi * len(self.successive_differences)), index=self._timeseries.index)
        # spectral generating function
        n = len(self.successive_differences)
        const_matrix = nm.empty(shape=(n, 2))
        const_matrix[:, 0] = 2 * (1 - nm.cos(2 * nm.pi *
                                             nm.linspace(start=0, stop=n - 1, num=n) / n))
        const_matrix[:, 1] = 1
        self._spectral_matrix = const_matrix * nm.array([[1, 1]])

    def FitTimeseries(self):
        self._scaled_variance = 1e6 * (self._timeseries.var(skipna=True) / 100)
        self._series_mean = self._timeseries.mean(
            skipna=True, numeric_only=True)
        first_value = self._timeseries.loc[[
            self._timeseries.first_valid_index()]].values.item(0)
        self._spectral_density = pd.DataFrame(data=nm.fft.fft(self.successive_differences)**2 /
                                              (2 * nm.pi * len(self.successive_differences)), index=self._timeseries.index)
        # spectral generating function
        n = len(self.successive_differences)
        const_matrix = nm.empty(shape=(n, 2))
        const_matrix[:, 0] = 2 * (1 - nm.cos(2 * nm.pi *
                                             nm.linspace(start=0, stop=n - 1, num=n) / n))
        const_matrix[:, 1] = 1
        self._spectral_matrix = const_matrix * nm.array([[1, 1]])
