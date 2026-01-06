import numpy as np
import matplotlib.pyplot as plt
from kalman_1d import KalmanFilterPosVel
from pathlib import Path

PROJECT_NAME = "Kalman Controller"
DEFAULT_OUT = Path(f"data/robotics/{PROJECT_NAME}")

np.random.seed(42)

# ---- Simulation settings ----
dt = 1.0
num_steps = 50

true_pos = 0.0
true_vel = 1.0

process_accel_std = 0.2      # how "jerky" the true motion is
measurement_noise_std = 1.0  # sensor noise

# ---- Kalman Filter settings ----
kf = KalmanFilterPosVel(
    dt=dt,
    initial_position=0.0,
    initial_velocity=0.0,
    initial_uncertainty=10.0,
    accel_variance=process_accel_std**2,
    measurement_variance=measurement_noise_std**2
)

# ---- Storage ----
true_positions = []
true_velocities = []
measurements = []
est_positions = []
est_velocities = []

for t in range(num_steps):
    # (Optional) change velocity mid-run to prove it adapts
    if t == 25:
        true_vel = 2.0  # kid starts "running"

    # True motion: pos += vel*dt + accel_noise
    accel_noise = np.random.normal(0, process_accel_std)
    true_pos = true_pos + true_vel * dt + 0.5 * accel_noise * dt * dt
    true_vel = true_vel + accel_noise * dt

    # Measurement: noisy position only
    z = true_pos + np.random.normal(0, measurement_noise_std)

    # Kalman steps
    kf.predict()
    x_est = kf.update(z)

    # Save
    true_positions.append(true_pos)
    true_velocities.append(true_vel)
    measurements.append(z)

    est_positions.append(float(x_est[0, 0]))
    est_velocities.append(float(x_est[1, 0]))

# saving
DEFAULT_OUT.mkdir(parents=True, exist_ok=True)

# ---- Plot position ----
plt.figure(figsize=(10, 5))
plt.plot(true_positions, label="True Position")
plt.scatter(range(num_steps), measurements, label="Measurements", alpha=0.5)
plt.plot(est_positions, label="Kalman Estimate (Position)", linewidth=2)
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.title("Kalman Filter (Position + Velocity State) — Position Estimate")
plt.legend()
plt.grid()

out_path = DEFAULT_OUT / "Position Estimate - Kalman 1D plot (week7).png"
plt.savefig(out_path, dpi=300) 

plt.show()

# ---- Plot velocity ----
plt.figure(figsize=(10, 5))
plt.plot(true_velocities, label="True Velocity")
plt.plot(est_velocities, label="Kalman Estimate (Velocity)", linewidth=2)
plt.xlabel("Time Step")
plt.ylabel("Velocity")
plt.title("Kalman Filter (Position + Velocity State) — Velocity Estimate")
plt.legend()
plt.grid()

out_path = DEFAULT_OUT / "Veocity Estimate- Kalman 1D plot (week7).png"
plt.savefig(out_path, dpi=300) 

plt.show()

print(f"Plot saved to: {out_path}")