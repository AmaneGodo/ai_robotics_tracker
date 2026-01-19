# Responsibility - Produce noisy measuremenets from the true system

import numpy as np

class Sensor:
    def __init__(self, measurement_std = 1.0):
        """
        Position sensor with Gaussian noise (normal distribution).

        measurement_std: standard deviation of measurement noise
        """

        self.measurement_std = measurement_std

    def measure(self, true_position):
        """
        Return a noisy measurement of position.

        true_position: actual position from the plant
        """

        noise = np.random.normal(0.0, self.measurement_std)

        # z = the noisy measurement of position produced by the sensor.
        z = true_position + noise

        return z

