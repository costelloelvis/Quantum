import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

try:
    # Use from_qasm_file directly so Qiskit can find the include files automatically
    qc = QuantumCircuit.from_qasm_file('dimple_qasm.qasm')
    
    print("File loaded successfully!")
    # print(qc.draw(output='text'))
    qc.draw(output='mpl', 
            idle_wires=False).savefig("Circuit.png")
    plt.show()

except FileNotFoundError:
    print('Error: "dimple_qasm.qasm" file not found. Check the file path.')
except Exception as e:
    print(f"An unexpected error occurred: {e}") 