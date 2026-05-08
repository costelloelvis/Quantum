from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# creaa a 2-qubit circuit
qc = QuantumCircuit(2)

# Initiate qubits to |00>
# Oracle for |11>
qc.cz(0,1)

# Grover Difussion Operator
qc.h([0,1])
qc.z([0,1])
qc.cz(0,1)
qc.h([0,1])

# Measure
qc.measure_all()

# Simulate
simulator = AerSimulator()
result=simulator.run(qc, shots=1024)
counts = result.result().get_counts(qc)
print(counts)