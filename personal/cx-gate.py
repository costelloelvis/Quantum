from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 2 qubits
qc = QuantumCircuit(2)

# Add a Hadamard Gate to Qubit 0
qc.h(0)

# Add a CNOT gate (control on qubit 0 , target on qubit 1)
qc.cx(0,1)

# Draw The Circuit
qc.draw(output='mpl')
plt.show()