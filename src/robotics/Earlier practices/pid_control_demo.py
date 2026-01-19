import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_NAME = "pid_control_demo"
DEFAULT_OUT = Path(f"data/projects/{PROJECT_NAME}")

# ================================================
# 🎯 GOAL:
# Compare multiple PID settings on one graph
# ================================================

target = 10.0
dt = 0.1
steps = 150

# 🧪 Different PID settings to test
pid_configs = [
    {"Kp": 0.4, "Ki": 0.00, "Kd": 0.00, "label": "P only"},
    {"Kp": 0.4, "Ki": 0.05, "Kd": 0.00, "label": "PI"},
    {"Kp": 0.4, "Ki": 0.05, "Kd": 0.2,  "label": "PID"},
]

# --- Create output directory ---
plot_dir = DEFAULT_OUT / "plots"
plot_dir.mkdir(parents=True, exist_ok=True)

# --- Generate plot ---
plt.figure(figsize=(8,5))

for cfg in pid_configs:
    pos = 0.0
    integral = 0.0
    prev_error = 0.0
    positions = []

    for _ in range(steps):
        error = target - pos
        integral += error * dt
        derivative = (error - prev_error) / dt

        control_output = (
            cfg["Kp"] * error +
            cfg["Ki"] * integral +
            cfg["Kd"] * derivative
        )

        pos += control_output * dt
        positions.append(pos)
        prev_error = error

    plt.plot(positions, label=cfg["label"])

plt.axhline(target, color='r', linestyle='--', label="Target")
plt.title("PID Tuning Comparison: P vs PI vs PID")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.legend()
plt.grid(True)

# --- Save before showing (safe) ---
out_path = plot_dir / "pid_tuning_comparison.png"
plt.savefig(out_path, dpi=300)

# --- Display plot ---
plt.show()

print(f"Plot saved to: {out_path}")
