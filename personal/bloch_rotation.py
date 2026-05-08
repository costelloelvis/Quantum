import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
from matplotlib.animation import FuncAnimation


# Rotate qubit around X-axis
angles = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(figsize=(5,5))

def update(angle):
    ax.clear()
    state = Statevector([np.cos(angle/2), np.sin(angle/2)])
    plot_bloch_multivector(state)
    plt.gca().set_title(f"Angle {angle:.2f}")

ani = FuncAnimation(fig, update, frames=angles, interval=50)
ani.save('bloch_rotation.gif', writer='pillow', fps=30)

plt.close(fig)