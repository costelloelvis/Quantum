from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

q_bell = QuantumCircuit(2, 2)
q_bell.barrier()
q_bell.h(0)
q_bell.cx(0, 1)
q_bell.barrier()
q_bell.measure([0, 1], [0,1])

q_bell.draw(output='mpl', plot_barriers=True)
plt.show()
