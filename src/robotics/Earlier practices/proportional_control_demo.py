import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
target = 10.0   # desired position
pos = 0.0       # initial positionn
Kp = 1     # proportional gain (try 0.1, 05, 1.0 later)
dt = 0.1        # time step
steps = 100     # number of simulation steps

# for storing results
positions = []
errors = []

# Simulation loop
for _ in range(steps):
    error = target - pos
    velocity = Kp * error
    pos += velocity * dt
    positions.append(pos)
    errors.append(error)

# plot position vs time
plt.figure(figsize=(6, 4))
plt.plot(positions, label = f'Kp = {Kp}')
plt.axhline(target, color = "r", linestyle="--", label = "Target")
plt.title("Proportional Control Motion Simulation")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()