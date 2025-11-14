import numpy as np
import json

sensor_data = {
    "timestamp": [1, 2, 3, 4, 5], 
    "temperature": [20.1, 20.4, 20.8, 21.0, 20.9],
    "distance": [100, 98, 97, 99, 101]
}

# store as JSON
json_str = json.dumps(sensor_data, indent = 2)
print("Raw JSON:\n", json_str)


# convert to NumPy arrays (llike robotics sensor processing)
time = np.array(sensor_data["timestamp"])
distance = np.array(sensor_data["distance"])
velocity = np.diff(distance) / np.diff(time)
print("\nEstimated velocity:", velocity)