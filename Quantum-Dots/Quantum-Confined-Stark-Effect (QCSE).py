import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Parameters (Typical values for a CdSe/ZnS Quantum Dot) ---
# Exciton Polarizability (alpha) in units of eV / (MV/cm)^2
# Order of magnitude is usually 10^-5 to 10^-3 Angstrom^3, 
# converted here for simpler field units.
# Assuming alpha_prime = 1/2 * alpha
alpha_prime = 5e-5  # Example value: 5 x 10^-5 eV / (MV/cm)^2

# Range of Electric Field (E) in MV/cm (Megavolts per centimeter)
E_min = 0.0
E_max = 1.0
num_points = 100

E_field = np.linspace(E_min, E_max, num_points)

# --- 2. Calculate Energy Shift (QCSE) ---
# Formula for the quadratic Stark shift (redshift):
# Delta E = - (1/2) * alpha * E^2, simplified to:
# Delta E = - alpha_prime * E^2 (where alpha_prime includes the 1/2 factor)
delta_E_pl = -alpha_prime * E_field**2

# Convert shift from eV to meV for better readability
delta_E_pl_meV = delta_E_pl * 1000 

# --- 3. Plotting the Result ---
plt.figure(figsize=(8, 5))
plt.plot(E_field, delta_E_pl_meV, color='red', linewidth=2)
plt.title('Quantum-Confined Stark Effect (QCSE) in Quantum Dots')
plt.xlabel('Electric Field, $E$ (MV/cm)')
plt.ylabel('PL Energy Shift, $\\Delta E_{PL}$ (meV)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.figtext(0.5, 0.01, f'Modeled using $\\Delta E_{{PL}} = -\\alpha\'E^2$, with $\\alpha\' = {alpha_prime}$ eV/(MV/cm)$^2$', 
            ha='center', fontsize=9, color='gray')
plt.show()