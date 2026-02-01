#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "State.h"

class Controller {
public:
    Controller();
    double update(const State& estimated_state);
};

#endif