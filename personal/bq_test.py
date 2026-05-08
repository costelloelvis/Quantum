import bluequbit
import cirq
from qiskit import QuantumCircuit

# Initialize client
bq_client = bluequbit.init("142EbsMhCDl0KM9VTSgGx7zCC7RmHQvJ")

# --- Cirq circuit ---
q0 = cirq.LineQubit(0)
cirq_circuit = cirq.Circuit([cirq.H(q0), cirq.measure(q0)])

cirq_result = bq_client.run(cirq_circuit)
print("Cirq result:", cirq_result)

# --- Qiskit circuit ---
qiskit_circuit = QuantumCircuit(1, 1)
qiskit_circuit.h(0)
qiskit_circuit.measure(0, 0)

qiskit_result = bq_client.run(qiskit_circuit)
print("Qiskit result:", qiskit_result)
