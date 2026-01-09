# Responsibility - Simulate the true system (what the robot is actually doing)
class Plant:
    def __init__(self, x0 = 0.0, v0 = 0.0, damping = 0.5, disturbance = -1.0):
        """
        1D plant (robot) with position and velocity.

        x0: initial position
        v0: initial velocity
        damping: velocity-proportional drag (friction)
        disturbance: constant external force (e.g., gravity/load)
        """

        self.x = x0
        self.v = v0
        self.damping = damping
        self.disturbance = disturbance


    def step(self, u, dt):
        """
        Advance the plant by one timestep.

        u: control input (force / acceleration command)
        dt: timestep
        """

        # acceleration = control input - (damping * velocity) + disturbance
        a = u - self.damping * self.v + self.disturbance

        # Integrate acceleration -> velocity
        self.v += a * dt

        # integrate velocity -> position
        self.x += self.v * dt

        return self.x, self.v