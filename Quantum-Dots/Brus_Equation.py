import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Physical Constants (SI Units)
# -----------------------------
hbar = 1.054e-34       # Reduced Planck constant (J·s)
e = 1.602e-19          # Electron charge (C)
epsilon_0 = 8.854e-12  # Vacuum permittivity (F/m)
pi = np.pi

# -----------------------------
# Material Parameters (Example: CdSe Quantum Dot)
# -----------------------------
Eg_bulk = 1.74 * e     # Bulk bandgap (J) (CdSe ~1.74 eV)

me_eff = 0.13 * 9.11e-31   # Electron effective mass
mh_eff = 0.45 * 9.11e-31   # Hole effective mass

epsilon_r = 9.5
epsilon = epsilon_r * epsilon_0

# Reduced mass
mu = (me_eff * mh_eff) / (me_eff + mh_eff)

# -----------------------------
# Radius Range (1 nm to 10 nm)
# -----------------------------
R_nm = np.linspace(1, 10, 200)   # in nm
R = R_nm * 1e-9                  # convert to meters

# -----------------------------
# Brus Equation Components
# -----------------------------

# (1) Blue-shift (Confinement Energy)
E_conf = (hbar**2 * pi**2) / (2 * R**2) * (1/me_eff + 1/mh_eff)

# (2) Red-shift (Coulomb Interaction)
E_coulomb = -(1.8 * e**2) / (4 * pi * epsilon * R)

# (3) Rydberg Energy (Exciton Binding)
E_rydberg = -(mu * e**4) / (2 * (4 * pi * epsilon)**2 * hbar**2)

# Total Energy (Absorption Energy)
E_total = Eg_bulk + E_conf + E_coulomb + E_rydberg

# -----------------------------
# Emission Energy (Stokes Shift)
# -----------------------------
E_relax = 0.05 * e   # ~0.05 eV relaxation loss
E_emission = E_total - E_relax

# -----------------------------
# Convert J → eV for plotting
# -----------------------------
J_to_eV = 1 / e

E_total_eV = E_total * J_to_eV
E_emission_eV = E_emission * J_to_eV
E_conf_eV = E_conf * J_to_eV
E_coulomb_eV = E_coulomb * J_to_eV
Eg_bulk_eV = Eg_bulk * J_to_eV

# -----------------------------
# Plot 1: Energy vs Radius
# -----------------------------
plt.figure()
plt.plot(R_nm, E_total_eV, label="Absorption Energy")
plt.plot(R_nm, E_emission_eV, '--', label="Emission Energy")
plt.axhline(Eg_bulk_eV, linestyle=':', label="Bulk Bandgap")

plt.xlabel("Quantum Dot Radius (nm)")
plt.ylabel("Energy (eV)")
plt.title("Energy vs Quantum Dot Radius (Brus Equation)")
plt.legend()
plt.grid()

# -----------------------------
# Plot 2: Contributions
# -----------------------------
plt.figure()
plt.plot(R_nm, E_conf_eV, label="Blue-shift (Confinement)")
plt.plot(R_nm, E_coulomb_eV, label="Red-shift (Coulomb)")

plt.xlabel("Quantum Dot Radius (nm)")
plt.ylabel("Energy (eV)")
plt.title("Energy Contributions vs Radius")
plt.legend()
plt.grid()

# -----------------------------
# Plot 3: Bandgap vs Radius
# -----------------------------
plt.figure()
plt.plot(R_nm, E_total_eV, label="Effective Bandgap")

plt.xlabel("Quantum Dot Radius (nm)")
plt.ylabel("Bandgap Energy (eV)")
plt.title("Bandgap vs Quantum Dot Radius")
plt.legend()
plt.grid()

plt.show()