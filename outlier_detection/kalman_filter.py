class KalmanFilter(object):

    def __init__(self, process_variance, estimated_measurement_variance):
        self.process_variance = process_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def negetive_log_likelihood(self, measurement):
        return 1.0

    def get_latest_estimated_measurement(self):
        return self.posteri_estimate