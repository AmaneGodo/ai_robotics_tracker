# Responsibility: Estimate position and velocity from noisy measurement

import numpy as np

class KalmanFilter:
    def __init__(self, dt, process_var = 1.0, measurement_var = 1.0):
        """
        1D Kalman filter estimating position and velocity.

        dt: timestep
        process_var: variance of process noise (model uncertainty)
        measurement_var: variance of measurement noise (sensor uncertainty)
        """

        self.dt = dt

        # State estimate [position, velocity]
        self.x_hat = np.array([[0.0], 
                              [0.0]])
        
        # State covariance (uncertainty)
        self.P = np.eye(2)

        # State transition matrix (constant velocity model)
        self.F = np.array([[1.0, dt], 
                          [0.0, 1.0]])
        
        # Control input model (acceleration affects velocity)
        self.B = np.array([[0.5 * dt**2],
                          [dt]])
        
        # Measurement model (acceleration affects velocity)
        self.H = np.array([[1.0, 0.0]])

        # Process noise covariance
        self.Q = process_var * np.array([
            [dt**4 / 4, dt**3 / 2],
            [dt**3 / 2, dt**2]
            ])
       
        # Measurement noise covariance
        self.R = np.array([[measurement_var]])

        # Identity matrix
        self.I = np.eye(2)

    def predict(self, u):
        """
        Prediction step (model-based)
        """

        # peredict state
        self.x_hat = self.F @ self.x_hat + self.B * u

        # predict uncertainty
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        """
        Correction step (measurement-based)
        """

        # innovation (measurement residual)
        y = z - (self.H @ self.x_hat)

        # innovation covariance
        S = self.H @ self.P @ self.H.T + self.R

        # Kalman gain
        K = self.P @ self.H.T @ np.linalg.inv(S)

        # Update state estimate
        self.x_hat = self.x_hat + K @ y

        # Updayte uncertainty
        self.P = (self.I - K @ self.H) @ self.P

    def get_state(self):
        """
        Return estimated position and velocity
        """

        return self.x_hat[0, 0], self.x_hat[1, 0]