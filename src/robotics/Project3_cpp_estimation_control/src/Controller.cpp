#include <iostream>
#include "Controller.h"

Controller::Controller() {}

double Controller::update(const State& estimated_state) {
    // Proportional-Derivative (PD) control
    // Goal: drive position toward zero while damping velocity to reduce overshoot

    double kp = 0.1;    // Position gain: pulls system toward target
    double kd = 0.05;   // Velocity gain: damps motion to prevent overshoot

    // Control law:
    // u = -kp * position - kd * velocity
    double u = -kp * estimated_state.position - kd * estimated_state.velocity;

    std::cout << "[Controller] u=" << u << "\n";
    return u;
}