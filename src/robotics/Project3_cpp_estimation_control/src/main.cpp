#include <iostream>
#include "Plant.h"
#include "Estimator.h"
#include "Controller.h"

// Main control loop:
// Plant -> Estimator -> Controller -> Plant
// Mirrors a real estimation–control pipeline

int main() {
    std::cout << "System starting...\n";
    Plant plant;
    Estimator estimator;
    Controller controller;

    double control = 0.0;
    for (int k=0; k < 10; ++k) {
        std::cout << "\n--- step " << k << "---\n";

        State measurement   = plant.update(control);
        State estimate      = estimator.update(measurement);
        control             = controller.update(estimate);
    }

    return 0;
}
