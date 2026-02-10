#include <iostream>
#include "Plant.h"
#include "Estimator.h"
#include "Controller.h"

// Main control loop:
// Plant -> Estimator -> Controller -> Plant
// Mirrors a real estimation–control pipeline

int main() {
    double dt = 0.01;   // 10 ms timestep → 100 Hz loop

    std::cout << "System starting...\n";
    Plant plant;
    Estimator estimator(0.2, 0.1, dt);
    Controller controller(0.1, 0.05, 2, -2); // (kp, kd, u_max, u_min)

    double u = 0.0;     // control input

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
