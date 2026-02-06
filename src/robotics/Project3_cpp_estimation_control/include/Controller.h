#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "State.h"

// Controller implements a simple PD control law.
// Control gains are owned by the Controller object and
// initialized once via the constructor.
class Controller {
public:
    // Constructor allows control gains to be configured at creation
    Controller(double kp = 0.1, double kd = 0.05);

    // Compute control input based on estimated state
    double update(const State& estimated_state);

private:
    double kp_; // Proportional gain (position correction)
    double kd_; // Derivative gain (velocity damping)
};

#endif