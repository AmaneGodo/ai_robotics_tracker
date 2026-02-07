#include <iostream>
#include "Plant.h"

Plant::Plant() {
    // Discrete-time plant dynamics:
    // The state is advanced before being printed, so step 0 reflects
    // the state after one update (not the raw initial condition).
    true_state_.position = 5.0; // initial disturbance
    true_state_.velocity = 1.0;
}

State Plant::update(double control_input, double dt) {
    // Dummy deterministic update
    true_state_.velocity += control_input * dt;
    true_state_.position += true_state_.velocity * dt;

    return true_state_;
}
