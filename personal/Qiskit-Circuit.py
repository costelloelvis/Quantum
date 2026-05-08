from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

q_circ = QuantumCircuit(4, 4)
q_circ.x([0,1])
q_circ.barrier()
q_circ.cx(1,2)
q_circ.cx(0,2)
q_circ.ccx(0,1,3)
q_circ.barrier()
q_circ.measure([2, 3], [0, 1])

q_circ.draw(output = 'mpl', plot_barriers=True)
plt.show()
