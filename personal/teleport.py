from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create circuit (3 qubits, 3 classical bits)
qc = QuantumCircuit(3, 3)

# Step 1: Prepare state to teleport (|ψ⟩)
qc.h(0)  # example state

# Step 2: Create entanglement
qc.h(1)
qc.cx(1, 2)

# Step 3: Bell measurement
qc.cx(0, 1)
qc.h(0)

# Measure Alice's qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Step 4: Conditional operations (Bob reconstructs state)
qc.cx(1, 2)
qc.cz(0, 2)

# Measure Bob’s qubit
qc.measure(2, 2)

# Simulate
sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1000).result()

counts = result.get_counts()
print(counts)

# Draw circuit
print(qc.draw())