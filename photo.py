
import os
os.chdir("C:/Users/feips/Desktop")

import matplotlib.pyplot as plt
import random
import numpy as np

# Number of points in the fern
num_points = 2000

# Define the transformations
transforms = [
    (0.85, 0.04, 0.00, -0.04, 0.85, 1.60, 0.85),  # Probability 0.85
    (0.20, -0.26, 0.00, 0.23, 0.22, 1.60, 0.07),  # Probability 0.07
    (-0.15, 0.28, 0.00, 0.26, 0.24, 0.44, 0.07),  # Probability 0.07
    (0.00, 0.00, 0.00, 0.00, 0.16, 0.00, 0.01)    # Probability 0.01
]

# Initialize starting point
x, y = 0, 0
points = []

# Generate points
for _ in range(num_points):
    r = random.random()
    sum_prob = 0
    for a, b, c, d, e, f, prob in transforms:
        sum_prob += prob
        if r <= sum_prob:
            x_new = a * x + b * y + c
            y_new = d * x + e * y + f
            x, y = x_new, y_new
            break
    points.append((x, y))

# Plotting
x_vals, y_vals = zip(*points)
plt.figure(figsize=(18, 28))  # Adjust size for high resolution
plt.scatter(x_vals, y_vals, color='green', s=0.1, marker='.')
plt.axis('off')

# Save the figure as a JPG file
plt.savefig('fern.jpg', dpi=300, bbox_inches='tight', pad_inches=0)

# Display the plot
plt.show()