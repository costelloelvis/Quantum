from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Shor

# Factor N = 15
N = 15
a = 2  # Choose a coprime to N

# Run Shor's
simulator = AerSimulator()
shor = Shor()
result = shor.factor(simulator, N, a)
print(f"Factors of {N}: {result.factors}")
