#ifndef ESTIMATOR_H
#define ESTIMATOR_H

#include "State.h"

class Estimator {
public: 
    Estimator();
    State update(const State& measurement);

private:
    State estimated_state_;    
};

#endif