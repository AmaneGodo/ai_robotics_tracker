#include <iostream>
#include "Controller.h"

Controller::Controller(double kp, double kd)
    : kp_(kp), kd_(kd) {}
    // Control gains are stored as member variables so they persist
    // across updates and can be tuned independently of control logic.

double Controller::update(const State& estimated_state) {
    // Proportional-Derivative (PD) control
    // Goal: drive position toward zero while damping velocity to reduce overshoot

    // Control law:
    // u = -kp * position - kd * velocity
    //  - proportional term pulls position toward target
    //  - derivative term damps velocity to reduce overshoot
    double u = -kp_ * estimated_state.position - kd_ * estimated_state.velocity;

    return u;
}