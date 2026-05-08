from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a simple Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run an ideal simulator
ideal_sim = AerSimulator()
ideal_result = ideal_sim.run(qc).result()
counts_ideal = ideal_result.get_counts()

print(f"Ideal Counts: '\n' {counts_ideal}")