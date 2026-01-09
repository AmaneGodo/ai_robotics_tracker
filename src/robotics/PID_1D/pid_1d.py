import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.1
steps = 1000
target = 10.0

# PID gains (start simple)
Kp = 1
Ki = 0.15
Kd = 0.5

damping = 0.5

# State
x = 0.0      # position
v = 0.0      # velocity

# PID state
integral_error = 0.0
prev_error = 0.0

# History for plotting
xs = []

for _ in range(steps):
    error = target - x
    integral_error += error * dt
    derivative_error = (error - prev_error) / dt

    # PID control input
    u = Kp * error + Ki * integral_error + Kd * derivative_error

    # System update
    disturbance = -1.0 # constant pull (like gravity or load)
    v += (u + disturbance - v * damping)* dt
    x += v * dt

    xs.append(x)
    prev_error = error

# Plot result
plt.plot(xs, label="Position")
plt.axhline(target, color="r", linestyle="--", label="Target")
plt.xlabel("Time step")
plt.ylabel("Position")
plt.title("1D PID Control — Position Tracking")
plt.legend()
plt.show()
