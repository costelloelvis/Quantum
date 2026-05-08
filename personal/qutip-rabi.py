from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Pauli-X Hamiltonian (1-qubit)
H = 0.5 * 2 * np.pi * sigmax()

# Initial state |0>
psi0 = basis(2, 0)

# Time evolution
tlist = np.linspace(0, 2, 100)
result = mesolve(H, psi0, tlist, [], [sigmax(), sigmay(), sigmaz()])

# Plot expectation values
plt.plot(tlist, result.expect[0], label="X")
plt.plot(tlist, result.expect[1], label="Y")
plt.plot(tlist, result.expect[2], label="Z")
plt.xlabel("Time")
plt.ylabel("Expectation values")
plt.legend()
plt.show()
