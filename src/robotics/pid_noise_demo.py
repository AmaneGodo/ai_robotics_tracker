import numpy as np
import matplotlib.pyplot as plt

def simulate_pid_with_noise():
    # 1) Simulation parameters
    target = 10.0
    dt = 0.1
    steps = 150

    # 2) True state
    true_pos = 0.0
    true_positions = []

    # 3) Measured state (sensor reading)
    measured_positions = []

    # 4) PID state variables
    Kp = 0.5
    Ki = 0.08
    Kd = 0.05
    integral = 0.0
    prev_error = 0.0
    pid_output_positions = []

    for _ in range(steps):
        # === a) Sensor simulation ===
        noise = np.random.normal(0, 0.3)
        measured = true_pos + noise
        
        # === b) PID computation using MEASURED not TRUE ===
        error = target - measured
        integral += error * dt
        derivative = (error - prev_error) / dt
            # The derivative error is very sensitive withh noise
            # This is why robots need:
                # Fiters (Kalman filters, low-pass filters)
                # smoother snesors
                # Lower Kd Values
                # Sensor fusion

        control = Kp * error + Ki * integral + Kd * derivative

        # === c) True physics update ===
        true_pos += control * dt

        # === d) Record for plotting ===
        # append lists here
        true_positions.append(true_pos)
        measured_positions.append(measured)
        pid_output_positions.append(control)

        # === e) Setup next loop ===
        prev_error = error

    # === Plotting ===
    plt.figure(figsize=(10, 5))

    plt.plot(true_positions, label = "True Position", linewidth=2)
    plt.plot(measured_positions, label = "Measured Position", linewidth = 2)
    plt.plot(pid_output_positions, label = "PID Output / Corrected", linestyle = "--")

    plt.title("PID Response withh Sensor Noise")
    plt.xlabel("Time Step")
    plt.ylabel("Position / Control Output")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    simulate_pid_with_noise()

if __name__ == "__main__":
    main()
