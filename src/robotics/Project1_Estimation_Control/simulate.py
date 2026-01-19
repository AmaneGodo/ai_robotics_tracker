# Responsibility - Wire everything together

import numpy as np
import matplotlib.pyplot as plt

from plant import Plant
from sensor import Sensor
from kalman_filter import KalmanFilter
from pid_controller import PIDController
from pathlib import Path

PROJECT_NAME = "Estimation Control"
DEFAULT_OUT = Path(f"data/robotics/{PROJECT_NAME}")

# -----------------------------
# Simulation parameters
# -----------------------------
dt = 0.1
sim_time = 20.0
steps = int(sim_time/dt)

target_position = 10.0

# -----------------------------
# Create system components
# -----------------------------
plant = Plant(x0=0.0, v0=0.0, damping=0.5, disturbance=-1.0)

sensor = Sensor(measurement_std = 1.0)

kalman = KalmanFilter(dt=dt, process_var=3, measurement_var=0.8)

controller = PIDController(target=target_position, kp=2, ki=0.3, kd=0.8)

# -----------------------------
# Initial state
# -----------------------------
u = 0.0

# -----------------------------
# Logging for plots
# -----------------------------
true_positions = []
measured_positions = []
estimated_positions = []
estimated_velocities = []
control_inputs = []

# -----------------------------
# Main simulation loop
# -----------------------------
for _ in range(steps):
    # 1. Plant evolves using LAST control input
    x_true, v_true = plant.step(u, dt)

    # 2. Sensor measures the true state
    z = sensor.measure(x_true)

    # 3. Kalman prediction (uses same control input)
    kalman.predict(u)

    # 4. Kalman correction (uses measurement)
    kalman.update(z)

    # 5. Get estimated state
    x_hat, v_hat = kalman.get_state()

    # 6. Controller computes NEXT control input
    u = controller.compute(x_hat, v_hat, dt)

    # log data
    # print(np.mean(z - x_true))
    true_positions.append(x_true)
    measured_positions.append(z)
    estimated_positions.append(x_hat)
    estimated_velocities.append(v_hat)
    control_inputs.append(u)

# -----------------------------
# Plot results
# -----------------------------
time = np.arange(steps) * dt

# -----------------------------
# Robotics behavior
# -----------------------------
DEFAULT_OUT.mkdir(parents=True, exist_ok=True)
plt.figure(figsize=(10, 5))
plt.plot(time, true_positions, label="True Position")
plt.plot(time, measured_positions, '.', alpha=0.4, label="Measured Position")
plt.plot(time, estimated_positions, label="Estimated Position")
plt.axhline(target_position, color="r", linestyle="--", label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.title("Kalman + PID Position Control")
plt.legend()
plt.grid()

out_path = DEFAULT_OUT / "Robotics Behavior by Kalamn filter and PID controller.png"
plt.savefig(out_path, dpi=300)
plt.show()

# -----------------------------
# Controller Input
# -----------------------------
plt.figure()
plt.plot(time, control_inputs)
plt.title("Control Input (u)")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration / Force")
plt.grid()

out_path = DEFAULT_OUT / "Control Input vs time.png"
plt.savefig(out_path, dpi = 300)
plt.show()
