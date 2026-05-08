from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Circuit WITHOUT measurement (for statevector)
qc = QuantumCircuit(1)
qc.h(0)

# Get statevector
state = Statevector.from_instruction(qc)

# Sample measurements
counts = state.sample_counts(1024)

# Add measurement only for display
qc_meas = qc.copy()
qc_meas.measure_all()

print(qc_meas.draw())

# Plot results
plot_histogram(counts)
plt.show()
