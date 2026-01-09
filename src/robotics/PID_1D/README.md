# 1D PID control and estimation

## Overview
This project simulates a PID controller to study how system behavior changes as the proportional (Kp), integral (Ki), and derivative (Kd) gains are adjusted. Through simulation, the project demonstrates how each gain affects stability, oscillation, settling behavior, and steady-state error.

The project also explores the relationship between PID control and Kalman filtering, highlighting how state estimation and control work together in real robotic systems.

## Kalman Filter and State Estimation
The Kalman filter is used to estimate the current state of a system from noisy sensor measurements and a prediction model. Sensors alone are not sufficient for control because they are inherently noisy and imperfect, and assuming the true system state directly from raw sensor data can lead to unstable or unsafe control behavior.

The Kalman filter improves control by producing an unbiased and smoothed estimate of the current state, which serves as a reliable reference for the controller. By using the estimated state rather than raw sensor data, the controller computes more accurate errors and generates more stable control inputs.

In a typical control loop:
    - The Kalman filter estimates the system’s current state
    - The PID controller uses that estimate and a target setpoint to compute control input

## PID Controller Behavior
The PID controller determines how much control input is applied based on the error between the target and the estimated system state.

    - Proportional (P):
        Provides the main driving force that pushes the system toward the target based on the current error.

    -  Integral (I):
        Eliminates steady-state error by accumulating past error over time. Integral control is necessary when constant disturbances or biases (such as gravity or friction) prevent the system from reaching the target.

    - Derivative (D):
        Reacts to how fast the error is changing and acts as a damping term. Derivative control reduces overshoot and oscillation by effectively applying a braking force.

## Damping and Steady-State Error
Damping plays a critical role in system stability. Without damping, a second-order system will oscillate indefinitely due to inertia. Physical damping (such as friction or drag) removes energy from the system, allowing oscillations to decay and the system to settle at the target.

Integral control is only required when the system experiences a constant disturbance. For example, gravity introduces a constant downward force that causes steady-state error. Without integral action, the system will settle below the target. The integral term accumulates this persistent error and generates the additional control effort required to cancel the disturbance.

## Key Insight
Kalman filtering and PID control serve different but complementary roles:
    - Kalman filter: estimates what is happening
    - PID controller: decides what to do about it

Together, they form the foundation of modern robotics control systems.
This architecture mirrors real robotic systems used in autonomy, navigation, and motion control.