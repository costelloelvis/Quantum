import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

# Define a harmonic oscillator
H = qt.destroy(2).dag()*qt.destroy(2)
times = np.linspace(0, 10, 100)

#Collapse operators(e.g., decay)
c_ops = [np.sqrt(0.1)*qt.destroy(2)]

#Initial state
rho_0 = qt.basis(2,1)*qt.basis(2,1).dag()

#Solve the Master Equation
result = qt.mesolve(H, rho_0, times, c_ops,[qt.num(2)])

#Plot the results
# qt.plot_expectation_values(result)
plt.plot(times, result.expect[0])
plt.xlabel('Time')
plt.ylabel('Occupation Probability')
plt.show()