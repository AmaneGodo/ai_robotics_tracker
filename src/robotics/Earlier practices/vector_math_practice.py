import numpy as np
import matplotlib.pyplot as plt

# Define two 3D vectors
a = np.array([2, 1, 3])
b = np.array([1, 4, 2])

print("Vector a: ", a)
print("Vector b: ", b)

# Compute magnitude (length) of a vector
magnitude_a = np.linalg.norm(a) # default function from numpy to calculate the magnitude of a vector
print("Magnitude of a = ", magnitude_a)

# Dot product - manual
manual_dot_product = sum(a[i] * b[i] for i in range(3))
print("Manual dot product: ", manual_dot_product)

# Dot product - numpy
numpy_dot_product = np.dot(a, b)
print("NumPy dot product: ", numpy_dot_product)

# Cross product - manual
manual_cross_product = np.array([
    a[1]*b[2] - a[2]*b[1],
    a[2]*b[0] - a[0]*b[2],
    a[0]*b[1] - a[1]*b[0]
])
print("Manual cross product: ", manual_cross_product)

# Cross product - NumPy
numpy_cross_product = np.cross(a, b)
print("NumPy cross product : ", numpy_cross_product)

# simullate motion
t = np.linspace(0, 10, 100)                                                     # time 0 to 10, 100 equal spacings
x = 2 * t                                                                       # velocity in x direction
y = 1.5 * t + 2 * np.sin(t)                                                     # velocity in y direction
velo_x = np.gradient(x, t)                                                      # dx/dt - numpy
velo_y = np.gradient(y, t)                                                      # dy/dt - numpy

#plot
plt.figure(figsize = (6, 6))                                                    # prepare the figure/canvas to plot on, 6x6 inches
plt.plot(x, y, label = "Motion path", color = "blue")                           # plot the positions, (x, y), also include motion path label on top left
plt.scatter(x[0], y[0], color='green', label='Start')                           # plot the starting position with a green point
plt.scatter(x[-1], y[-1], color='red', label='End')                             # plot the ending position with a red point 
    # draw arrows every 10th point
plt.quiver(x[::10], y[::10], velo_x[::10], velo_y[::10],                        # .quiver() draws arrows (x, y, velo_x, velo_y) at given position
           color='red', scale=20, width=0.005, label="Velocity vectors")        # .quiver() need 4 inputs x-pos, y-pos, x_velo, y_velo
                                                                                    # x[::10], y[::10] - take every 10th point
                                                                                    # velo_x[::10], velo_y[::10] - corresponding velocity components
                                                                                    # scale = 20 - adjust arrow length scaling
                                                                                    # widthh = 0.005 - width of arrows
plt.xlabel("X position")                                                        # X axis label
plt.ylabel("Y position")                                                        # Y axis label
plt.title("2D Motion simulation")                                               # title
plt.legend()                                                                    # shows the “Motion path” label in a small box (usually top left or right).
plt.grid(True)                                                                  # show grid or not

plt.figure(figsize=(6,6))
plt.plot(x, y, 'b-', label='Motion path')

# Midpoint-corrected velocity visualization
xm = (x[:-1] + x[1:]) / 2
ym = (y[:-1] + y[1:]) / 2
plt.quiver(xm[::10], ym[::10], velo_x[::10], velo_y[::10],
           color='green', scale=20, width=0.005, label='Velocity (midpoint corrected)')

plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("2D Motion with Midpoint-Corrected Velocity Vectors")
plt.legend()
plt.grid(True)

plt.show()                                                                      # launches the interactive window (and blocks code until closed)

