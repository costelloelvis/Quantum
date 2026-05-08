import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

try:
    
    with open('qasm_test.qasm', 'r') as file:
        qasm_str = file.read().replace('include "qelib1.inc";', '')
        
        qc = QuantumCircuit.from_qasm_file(qasm_str)
        
except FileNotFoundError:
    print('Error: "qasm_test.qasm" file not found. Check the file path')

# Draw using matplotlib
qc.draw(output='mpl')
plt.show()
