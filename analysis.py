import numpy as np

import matplotlib.pyplot as plt

# Constants


k = 500  # Assuming k = 1 for simplicity (adjust if you have a different value)
d = 0.06

# Functions for F_1 and d_1 (numerical)
F_1 = lambda theta: k * d * (np.sqrt((1 - np.sin(theta))**2 + (3 - np.cos(theta))**2) - 1.5)
d_1 = lambda theta: np.sqrt(10) * d * np.sin(np.arctan((3 - np.cos(theta)) / (1 - np.sin(theta))) - np.arctan(3))

F_2 = lambda theta: k * d * (np.sqrt((1 - np.sin(theta))**2 + (3 + np.cos(theta))**2) - 1.5)
d_2 = lambda theta: np.sqrt(10) * d * np.sin(np.arctan((3 + np.cos(theta)) / (1 - np.sin(theta))) - np.arctan(3))

# Define theta as an array of values
theta_values = np.linspace(0, 2 * np.pi, 1000)  # theta goes from 0 to 2π radians

# Calculate product of F_1 and d_1
product = F_1(theta_values) * d_1(theta_values)
product2 = F_2(theta_values) * d_2(theta_values)
total_moment = product - product2

# Plot
plt.figure(figsize=(8, 6))
plt.plot(theta_values, product, label=r'$F_1(\theta) \cdot d_1(\theta)$', color='b')
plt.plot(theta_values, product2, label=r'$F_2(\theta) \cdot d_2(\theta)$', color='r')
plt.plot(theta_values, total_moment, label=r'total moment', color='black')
plt.title(r'Forces against angle $\theta$')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'Moment')
plt.legend()
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('plot.png')
# Show the plot
plt.show()

