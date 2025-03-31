import numpy as np

import matplotlib.pyplot as plt

# Constants


k = 1  # Assuming k = 1 for simplicity (adjust if you have a different value)
d = 0.06

# Functions for F_1 and d_1 (numerical)
F_1 = lambda theta: k * d * (np.sqrt((1 - np.sin(theta))**2 + (3 - np.cos(theta))**2) - 1.5)
d_1 = lambda theta: np.sqrt(10) * d * np.sin(np.arctan((3 - np.cos(theta)) / (1 - np.sin(theta))) - np.arctan(3))

# Define theta as an array of values
theta_values = np.linspace(0, 2 * np.pi, 1000)  # theta goes from 0 to 2π radians

# Calculate product of F_1 and d_1
product = F_1(theta_values) * d_1(theta_values)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(theta_values, product, label=r'$F_1(\theta) \cdot d_1(\theta)$', color='b')
plt.title(r'Product of $F_1(\theta)$ and $d_1(\theta)$ for $d = 0.06$')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'Product of $F_1$ and $d_1$')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()

