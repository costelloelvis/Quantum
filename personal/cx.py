from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc_ha = QuantumCircuit(4, 2)
qc_ha.x(0)
qc_ha.x(1)
qc_ha.barrier()

qc_ha.cx(0,2)
qc_ha.cx(1,2)
qc_ha.barrier()

qc_ha.measure(2, 0)
qc_ha.measure(3, 0)

qc_ha.draw(output="mpl")
plt.show()
