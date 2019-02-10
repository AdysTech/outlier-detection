# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

name = "outlier_detection"

from .detect_outliers import LevelShiftDetector
from .stsm import TimeSeriesModel
from .kalman_filter import KalmanFilter

__all__ = [
    'LevelShiftDetector',
    'TimeSeriesModel',
    'KalmanFilter'
]

__version__ = '0.0.1'