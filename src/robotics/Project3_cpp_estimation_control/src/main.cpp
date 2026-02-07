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

    double u = 0.0;     // control input
    double dt = 0.01;   // 10 ms timestep → 100 Hz loop

    State measurement;
    State estimate;

    for (int k=0; k < 1000; ++k) {
        measurement   = plant.update(u, dt);
        estimate      = estimator.update(measurement);
        u             = controller.update(estimate);

        if (k % 50 == 0) {
            std::cout << "\n--- step " << k << "---\n";
            std::cout << "[Plant] pos=" << measurement.position
              << " vel=" << measurement.velocity << "\n";
            std::cout << "[Estimator] est_pos=" << estimate.position
              << " est_vel=" << estimate.velocity << "\n";
            std::cout << "[Controller] u=" << u << "\n";
        }
    }

    return 0;
}
