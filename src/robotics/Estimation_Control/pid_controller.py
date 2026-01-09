# Responsibility - Compute control input to reach the target

class PIDController:
    def __init__(self, 
                 target, 
                 kp = 1.0,
                 ki = 0.0, 
                 kd = 0.5):
        """
        PID controller for 1D position control.

        target: desired position
        kp: proportional gain
        ki: integral gain
        kd: derivative gain
        """

        self.target = target
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral_error = 0.0

    def compute(self, x_hat, v_hat, dt):
        """
        Compute control input using estimated state.

        x_hat: estimated position
        v_hat: estimated velocity
        dt: timestep
        """

        # position error
        error = self.target - x_hat

        # integral of error
        self.integral_error += error * dt

        # PID control law
        # input (force/acceleration) = proportional term + integral term + derivative term (damping)
        u = self.kp * error + self.ki * self.integral_error - self.kd * v_hat

        return u