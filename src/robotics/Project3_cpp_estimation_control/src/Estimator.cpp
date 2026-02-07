#include <iostream>
#include "Estimator.h"

Estimator::Estimator() {
    estimated_state_.position = 0.0;
    estimated_state_.velocity = 0.0;
}

State Estimator::update(const State& measurement) {
    // Placeholder: copy measurement directly
    estimated_state_ = measurement;

    return estimated_state_;
}
