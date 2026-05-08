import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Decay Parameters ---
# Radiative lifetime (typical for QDs) in nanoseconds (ns)
tau_rad = 50.0 
Gamma_rad = 1.0 / tau_rad

# Auger lifetime (fast, non-radiative) in ns 
# This dominates the decay in a charged QD (e.g., a Trion)
tau_Auger = 0.5 
Gamma_Auger = 1.0 / tau_Auger

# Initial Excitation Population
N0 = 1.0
# Time vector in ns
t_max = 10.0
t_steps = 100
time = np.linspace(0, t_max, t_steps)

# --- 2. Calculate Decay Curves ---
# A. Charged QD (Trion): Dominated by Auger (Uniform Coulomb Potential effect)
# Total rate: Gamma_total_charged = Gamma_rad + Gamma_Auger
Gamma_total_charged = Gamma_rad + Gamma_Auger
N_charged = N0 * np.exp(-Gamma_total_charged * time)

# B. Neutral QD (Exciton): Dominated by Radiative decay (for comparison)
# Total rate: Gamma_total_neutral approx Gamma_rad (Auger is negligible)
Gamma_total_neutral = Gamma_rad 
N_neutral = N0 * np.exp(-Gamma_total_neutral * time)

# --- 3. Plotting the Decay ---
plt.figure(figsize=(8, 5))

# Plotting on a semi-log scale to show the exponential decay
plt.plot(time, N_neutral, label=f'Neutral Exciton ($\\tau$ = {tau_rad:.1f} ns)', 
         linestyle='--', color='blue')
plt.plot(time, N_charged, label=f'Charged Trion ($\\tau_{{eff}}$ = {1/Gamma_total_charged:.2f} ns)', 
         color='red', linewidth=2)

plt.yscale('log')
plt.title('Photoluminescence Decay Curves (PL Quenching by Auger)')
plt.xlabel('Time (ns)')
plt.ylabel('Normalized PL Intensity (Log Scale)')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.show()