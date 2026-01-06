# 1D Kalman Filter — Position & Velocity Estimation

## Overview
This project implements a 1D Kalman Filter to estimate the **position and velocity** of a moving system using **noisy position measurements**. The goal is to demonstrate how a system can maintain a stable and reliable estimate even when sensors and motion models are imperfect.

## Problem Statement
In real-world systems, sensor measurements are noisy and unreliable. Using raw sensor data directly can cause unstable and jittery estimates, making it difficult to reason about the true state of the system.

A reliable estimate is required for downstream tasks such as control and decision-making.

## Approach
The Kalman Filter combines two sources of information at every time step:
- A **prediction** from a motion model
- A **measurement** from a noisy sensor

By balancing these two sources based on their uncertainty, the filter produces an estimate that is both stable and responsive to changes.

## State Definition
The system state is defined as:

- Position  
- Velocity  

Including velocity in the state allows the filter to adapt more quickly when motion changes. If the system suddenly accelerates or decelerates, the filter can update its estimate rather than assuming constant motion.

## Prediction and Correction
### Prediction Step
The prediction step advances the state forward in time using a constant-velocity motion model. Because no new sensor data is used during this step, uncertainty increases.

### Correction Step
The correction step incorporates a noisy position measurement to adjust the estimate and reduce uncertainty.

## Kalman Gain
The Kalman Gain determines how much the filter trusts the sensor measurement relative to the prediction:
- **High Kalman Gain** → trust the sensor more  
- **Low Kalman Gain** → trust the prediction more  

This balance allows the filter to automatically adjust to changing system conditions.

## Noise Modeling
### Process Noise
Process noise represents uncertainty in the system dynamics, such as unmodeled acceleration or sudden changes in motion.

- Too low → slow adaptation  
- Too high → noisy estimates  

### Measurement Noise
Measurement noise represents sensor unreliability. When sensor noise increases, the filter relies more on prediction and becomes more uncertain overall.

## Stability and Adaptation
When the system behavior is consistent, uncertainty decreases and the estimate becomes smooth and stable. When the system behavior changes, uncertainty temporarily increases, allowing the filter to adapt to the new motion.

## Failure Mode
A Kalman Filter can converge to an incorrect estimate if the sensor has a **consistent bias** that is not modeled. The filter reduces random noise but does not automatically correct systematic errors.

## Robotics Relevance
Kalman filtering is fundamental in robotics because physical systems operate in real time with noisy sensors and imperfect models. Accurate state estimation is essential for navigation, control, and autonomy.

## How to Run
```bash
python simulate.py
```
