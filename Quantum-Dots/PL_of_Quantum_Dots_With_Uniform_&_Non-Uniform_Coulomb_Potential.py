import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Quantum dot parameters
# ---------------------------
hbar = 1.054e-34       # J*s
e = 1.602e-19          # C
eps0 = 8.85e-12        # vacuum permittivity
eps = 10                # dielectric constant of QD
me = 0.13 * 9.11e-31    # electron effective mass
mh = 0.45 * 9.11e-31    # hole effective mass
Eg = 2.0 * e            # band gap (example: 2 eV)

# QD radius range (nm → meters)
R = np.linspace(1e-9, 8e-9, 200)

# ---------------------------
# Brus equation (without external potentials)
# ---------------------------
E_conf = (hbar**2 * np.pi**2) * (1/(2*me*R**2) + 1/(2*mh*R**2))
E_coul = -1.8 * e**2 / (4*np.pi*eps0*eps*R)
E_PL_base = Eg + E_conf + E_coul

# ---------------------------
# Uniform Coulomb Potential
# ---------------------------
# Adds constant shift (like uniform electric potential)
U_uniform = -0.05 * e    # uniform potential shift of -0.05 eV
E_PL_uniform = E_PL_base + U_uniform

# ---------------------------
# Non-uniform Coulomb Potential
# ---------------------------
# Modeled as a position-dependent Coulomb distortion
# stronger for smaller R because field is stronger
U_nonuniform = -0.3 * e * (1/R) / np.max(1/R)
E_PL_nonuniform = E_PL_base + U_nonuniform

# ---------------------------
# Convert to eV
# ---------------------------
to_eV = 1/e
E_PL_base_eV = E_PL_base * to_eV
E_PL_uniform_eV = E_PL_uniform * to_eV
E_PL_nonuniform_eV = E_PL_nonuniform * to_eV

# ---------------------------
# Plot results
# ---------------------------
plt.figure(figsize=(8,6))
plt.plot(R*1e9, E_PL_base_eV, label="No external potential", linewidth=2)
plt.plot(R*1e9, E_PL_uniform_eV, label="Uniform Coulomb potential", linestyle='--')
plt.plot(R*1e9, E_PL_nonuniform_eV, label="Non-uniform Coulomb potential", linestyle='-.')
plt.xlabel("Quantum dot radius (nm)")
plt.ylabel("PL energy (eV)")
plt.title("Quantum Dot Photoluminescence under Coulomb Potentials")
plt.legend()
plt.grid(True)
plt.show()
