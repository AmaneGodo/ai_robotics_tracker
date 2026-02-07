#ifndef PLANT_H
#define PLANT_H

#include "State.h"

class Plant {
public: 
    Plant();  
    State update(double control_input, double dt);

private:
    State true_state_;
};

#endif