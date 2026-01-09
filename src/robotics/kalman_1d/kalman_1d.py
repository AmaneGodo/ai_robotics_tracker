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
        # "At any moment, I believe the system is at position x and veocity v"
        self.x = np.array([[initial_position],
                           [initial_velocity]], dtype=float)

        # State covariance (uncertainty)
        # "How sure am I about positions and velocity?"
        self.P = np.eye(2) * initial_uncertainty

        # State transition matrix (constant velocity model)
        self.F = np.array([[1.0, dt],
                           [0.0, 1.0]], dtype=float)

        # Measurement matrix (we measure position only)
        self.H = np.array([[1.0, 0.0]], dtype=float)

        # Measurement noise covariance
        self.R = np.array([[measurement_variance]], dtype=float)

        # Process noise covariance (how much acceleration uncertainty you expect)
        # Asuming acceleration exists, but I don't model it explicitly -> treat acceleration as a noise.
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

        # Innovation / residual - how wrong was my prediction?
        y = z - (self.H @ self.x)

        # Innovation covariance - How uncertain was my predicted sensor reading?
        # S represents the total uncertainty of the innovation, combining prediction uncertainty and sensor noise
        S = self.H @ self.P @ self.H.T + self.R

        # Kalman Gain
        K = self.P @ self.H.T @ np.linalg.inv(S)

        # Update state and covariance
        self.x = self.x + (K @ y)
        self.P = (self.I - (K @ self.H)) @ self.P

        return self.x

