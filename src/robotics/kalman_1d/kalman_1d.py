import numpy as np

class KalmanFilterPosVel:
    """
    1D Kalman Filter with state = [position, velocity]^T
    Measurement z is position only.
    """

    def __init__(self, dt: float,
                 initial_position: float,
                 initial_velocity: float,
                 initial_uncertainty: float,
                 accel_variance: float,
                 measurement_variance: float):

        self.dt = dt

        # State vector [pos, vel]
        self.x = np.array([[initial_position],
                           [initial_velocity]], dtype=float)

        # State covariance (uncertainty)
        self.P = np.eye(2) * initial_uncertainty

        # State transition matrix (constant velocity model)
        self.F = np.array([[1.0, dt],
                           [0.0, 1.0]], dtype=float)

        # Measurement matrix (we measure position only)
        self.H = np.array([[1.0, 0.0]], dtype=float)

        # Measurement noise covariance
        self.R = np.array([[measurement_variance]], dtype=float)

        # Process noise covariance (how much acceleration uncertainty you expect)
        # This comes from modeling unknown acceleration as noise.
        q = accel_variance
        dt2 = dt * dt
        dt3 = dt2 * dt
        dt4 = dt2 * dt2
        self.Q = q * np.array([[dt4 / 4.0, dt3 / 2.0],
                               [dt3 / 2.0, dt2]], dtype=float)

        self.I = np.eye(2)

    def predict(self):
        # x = F x
        self.x = self.F @ self.x

        # P = F P F^T + Q
        self.P = self.F @ self.P @ self.F.T + self.Q

        return self.x

    def update(self, z: float):
        """
        z: scalar position measurement
        """
        z = np.array([[z]], dtype=float)

        # Innovation / residual
        y = z - (self.H @ self.x)

        # Innovation covariance
        S = self.H @ self.P @ self.H.T + self.R

        # Kalman Gain
        K = self.P @ self.H.T @ np.linalg.inv(S)

        # Update state and covariance
        self.x = self.x + (K @ y)
        self.P = (self.I - (K @ self.H)) @ self.P

        return self.x

