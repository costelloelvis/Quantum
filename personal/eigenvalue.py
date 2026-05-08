import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simple 1D wave function example
x = np.linspace(-3, 3, 400)
p = np.linspace(-3, 3, 400)
E = np.sqrt(p**2 + 1)  # energy relation

# Plotting 2D energy relation
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(p, E, label='E/mc²')
plt.xlabel('p/mc')
plt.ylabel('E/mc²')
plt.title('Mass Shell')
plt.legend()

# 3D wave representation (simplified)
X, P = np.meshgrid(x, p)
Z = np.sin(X) * np.cos(P)

ax = plt.subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, P, Z, cmap='rainbow')
plt.title('Wave Function Surface')
plt.show()
