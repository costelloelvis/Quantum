import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 1. Setup Times and Hamiltonian
# We increase 'times' density to see the actual path/rotation
times = np.linspace(0, 9, 100) 

# Define Hamiltonians that correspond to the gates
# H = omega * Operator. Here we use pi/2 strength to rotate over time.
H_gate = (qt.sigmax() + qt.sigmaz()) / np.sqrt(2) # Hadamard-like rotation
X_gate = qt.sigmax()
Y_gate = qt.sigmay()

# 2. Time-Dependent Hamiltonian (Using string format for efficiency)
# Each gate is active for a 3-unit time window
H_t = [[H_gate, '1*(t<=3)'], 
       [X_gate, '1*(t>3)*(t<=6)'], 
       [Y_gate, '1*(t>6)*(t<=9)']]

psi_0 = qt.basis(2, 0)
result = qt.sesolve(H_t, psi_0, times)

# 3. Prepare Bloch Sphere Animation
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
b = qt.Bloch(fig=fig, axes=ax)

def animate(i):
    ax.clear() # Clear the axes to prevent ghosting
    b.axes = ax
    b.clear()
    
    # Add all previous points to show the "trail"
    points = [qt.expect([qt.sigmax(), qt.sigmay(), qt.sigmaz()], state) for state in result.states[:i+1]]
    if points:
        p_x, p_y, p_z = zip(*points)
        b.add_points([p_x, p_y, p_z])
    
    b.add_states(result.states[i]) # Add current state vector
    b.render()
    return ax,
anim = animation.FuncAnimation(fig, animate, frames=len(times), interval=50, blit=False)
plt.show()