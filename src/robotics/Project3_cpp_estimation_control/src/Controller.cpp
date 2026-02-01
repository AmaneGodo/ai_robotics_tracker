#include <iostream>
#include "Controller.h"

Controller::Controller() {}

double Controller::update(const State& estimated_state) {
    // Dummy control: push toward zero
    double control = -0.1 * estimated_state.position;

    std::cout << "[Controller] u=" << control << "\n";
    return control;
}