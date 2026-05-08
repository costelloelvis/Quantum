import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# 1. Configuration: Let's try to generate 10 potential bits
n = 10 
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n) # 0 = Z, 1 = X

# 2. Alice prepares and "sends" the qubits
circuits = []
for i in range(n):
    qc = QuantumCircuit(1, 1)
    # Alice encodes her bit
    if alice_bits[i] == 1:
        qc.x(0)
    # Alice chooses a basis
    if alice_bases[i] == 1: # X-basis
        qc.h(0)
    circuits.append(qc)

# 3. Bob receives and measures in random bases
bob_bases = np.random.randint(2, size=n)
bob_results = []
simulator = AerSimulator()

for i in range(n):
    qc = circuits[i]
    if bob_bases[i] == 1: # Bob measures in X-basis
        qc.h(0)
    qc.measure(0, 0)
    
    # Run the simulation
    job = simulator.run(qc, shots=1, memory=True)
    result = job.result().get_memory()[0]
    bob_results.append(int(result))

# 4. Sifting: Alice and Bob compare bases (publicly)
sifted_key = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        sifted_key.append(alice_bits[i])

print(f"Alice's Bits:  {list(alice_bits)}")
print(f"Alice's Bases: {list(alice_bases)}")
print(f"Bob's Bases:   {list(bob_bases)}")
print(f"Shared Key:    {sifted_key}")
