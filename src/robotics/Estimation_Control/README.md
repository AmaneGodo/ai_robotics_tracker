# Kalman Filter + PID Control — 1D Position Control
This project demonstrates a complete **estimation + control pipeline** commonly used in robotics and autonomous systems.  
A noisy sensor measurement is filtered using a Kalman Filter to estimate the system state, and a PID controller uses that estimate to drive the system toward a target position.

This project focuses on correctness and clarity rather than optimal performance, mirroring how real robotic systems are incrementally developed and validated.

## Limitations of This Model
This project is intentionally designed as a **foundational control and estimation demo**, and therefore includes several simplifying assumptions:

- **Model mismatch:**  
  The Kalman Filter does not model constant disturbances (e.g., bias or external forces) present in the plant. As a result, the estimated state can remain slightly above the true state when unmodeled disturbances act on the system.
- **No bias estimation:**  
  The filter estimates only position and velocity. Sensor bias and constant disturbances are not included in the state vector, which limits long-term accuracy under persistent external forces.
- **Linear dynamics assumption:**  
  The system assumes linear motion and Gaussian noise. Nonlinear dynamics and non-Gaussian noise are not addressed in this implementation.
- **Manual PID tuning:**  
  PID gains are tuned empirically. The controller is not adaptive or optimal and does not adjust gains automatically based on system behavior.

Despite these limitations, the model captures the core interaction between **state estimation (Kalman filtering)** and **feedback control (PID)**, which is fundamental to real-world robotics systems.

These limitations were intentionally chosen to keep the project focused on foundational estimation and control concepts.

## System Overview
The simulation consists of four main components:

1. **Plant** — the physical system (true position and velocity)
2. **Sensor** — provides noisy position measurements
3. **Kalman Filter** — estimates position and velocity from noisy data
4. **PID Controller** — computes control input to reach a target

The system runs as a closed loop:
**Plant → Sensor → Kalman Filter → PID Controller → Plant**

## Plant (System Dynamics)
The plant represents the true physical system and follows basic kinematic rules:
- Velocity changes based on applied acceleration
- Position changes based on velocity
- Both position and velocity evolve **cumulatively over time**

This accumulation is critical for realistic motion modeling.

## Sensor Model
The sensor observes the plant’s true position and adds random noise to simulate real-world measurement uncertainty.  
Sensor measurements alone are unreliable and should not be used directly for control.

## Kalman Filter (State Estimation)
The Kalman Filter estimates the system’s **current state** (position and velocity) using:
- A motion model (prediction step)
- Noisy sensor measurements (correction step)

The Kalman Filter estimates the current state only and does not use the target; target tracking is handled entirely by the PID controller.

### Key Concepts
- **Prediction** increases uncertainty over time
- **Correction** reduces uncertainty using sensor data
- **Kalman Gain** balances trust between prediction and measurement

The filter adapts automatically when system behavior changes.

## PID Controller (Control)
The PID controller computes the control input (acceleration/force proxy) based on the error between target position and estimated position.
- error = target state - estimated state

### PID Terms
- **P (Proportional)** — drives the system toward the target
- **I (Integral)** — eliminates steady-state error caused by constant bias (e.g., gravity)
- **D (Derivative)** — dampens oscillations by reacting to rapid changes

The controller uses the **Kalman state estimate**, not raw sensor data, for safer and more stable control.

### Control Input Behavior
The control input initially spikes to reduce large position error, then gradually settles as the system approaches steady state.  
In the presence of constant disturbance, the controller maintains a nonzero steady control input to counteract external forces, which is consistent with real-world control behavior.

This plot highlights how estimation quality directly influences control effort in closed-loop systems.

## Why Estimation Improves Control
Raw sensor data is noisy and imperfect.  
Using a Kalman Filter provides a smoother, less biased estimate of the system state, allowing the PID controller to make better control decisions.

This separation of **estimation** and **control** reflects real robotics systems.

## Results
The simulation shows:
- Noisy sensor measurements scattered around the true state
- A smooth Kalman estimate tracking the true position
- Stable convergence toward the target using PID control

## How to Run
```bash
python simulate.py
```

## Tuning
### Process Noise vs Measurement Noise Tuning
In this simulation, the plant includes a constant disturbance that is not explicitly modeled in the Kalman Filter’s prediction step, initially causing steady-state error due to estimator–plant model mismatch. This creates a realistic model mismatch scenario commonly encountered in real robotic systems.

To improve estimator and control performance, the following tuning adjustments were made:
- Increased process noise variance (Q): 1.0 → 3.0
- Decreased measurement noise variance (R): 1.0 → 0.8

### Rationale
- Increasing process noise reflects lower confidence in the motion model due to unmodeled external forces.
- Slightly decreasing measurement noise allows the filter to rely more on sensor feedback.
- Together, this shifts the Kalman Gain to better balance prediction and measurement under disturbance.

### Result
- The estimated position tracks the true position more closely.
- The PID controller receives a more accurate state estimate.
- The true system position converges closer to the target despite constant disturbance.

## Key Insight
- When disturbances cannot be explicitly modeled, tuning process and measurement noise allows the estimator to remain robust without increasing model complexity.
- Estimator tuning directly impacts control performance; improving state estimation under model uncertainty enables more accurate and stable closed-loop control.