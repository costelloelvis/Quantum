import numpy as np
import matplotlib.pyplot as plt

L = np.linspace(1e-9, 5e-9, 50)
E = 1 / (L**2)

plt.plot(L, E)
plt.xlabel("Quantum Dot Size (m)")
plt.ylabel("Energy (arb units)")
plt.title("Quantum Confinement (Blue Shift)")
plt.grid()
plt.show()