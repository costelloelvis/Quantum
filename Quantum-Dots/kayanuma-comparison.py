import numpy as np
import matplotlib.pyplot as plt

# Constants
h_bar = 1.054e-34  # JÂ·s
e = 1.602e-19      # C
m_0 = 9.109e-31   # kg
eps_0 = 8.854e-12 # F/m

def calculate_kayanuma(R_nm, Eg_ev, epsilon, me_eff, mh_eff):
    R = R_nm * 1e-9
    mu = (me_eff * mh_eff) / (me_eff + mh_eff) * m_0
    
    # Kinetic Confinement term
    kinetic = (h_bar**2 * np.pi**2) / (2 * mu * R**2)
    # Coulomb Interaction term
    coulomb = (1.786 * e**2) / (4 * np.pi * eps_0 * epsilon * R)
    # Correlation term
    E_ry_star = (mu * e**4) / (2 * (4 * np.pi * eps_0 * epsilon)**2 * h_bar**2)
    correlation = 0.248 * E_ry_star
    
    E_ev = Eg_ev + (kinetic - coulomb - correlation) / e
    wavelength_nm = 1240 / E_ev
    return E_ev, wavelength_nm

# Material data dictionary
materials = {
    'CdSe': {'Eg': 1.74, 'eps': 10.6, 'me': 0.13, 'mh': 0.45},
    'CdS':  {'Eg': 2.42, 'eps': 5.7,  'me': 0.21, 'mh': 0.80},
    'ZnSe': {'Eg': 2.70, 'eps': 9.1,  'me': 0.17, 'mh': 0.60},
    'ZnS':  {'Eg': 3.68, 'eps': 8.3,  'me': 0.34, 'mh': 0.23}
}

radii = np.linspace(1.5, 8.0, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for name, p in materials.items():
    res = [calculate_kayanuma(r, p['Eg'], p['eps'], p['me'], p['mh']) for r in radii]
    energies, wavelengths = zip(*res)
    
    ax1.plot(radii, energies, label=name, linewidth=2)
    ax2.plot(radii, wavelengths, label=name, linewidth=2)

# Formatting Energy Plot
ax1.set_title('Energy Gap vs. Radius')
ax1.set_xlabel('Radius $R$ (nm)')
ax1.set_ylabel('Energy $E$ (eV)')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

# Formatting Wavelength Plot
ax2.set_title('Emission Wavelength vs. Radius')
ax2.set_xlabel('Radius $R$ (nm)')
ax2.set_ylabel('Wavelength $lambda$ (nm)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.axhspan(400, 700, color='gray', alpha=0.1) # Visible Spectrum highlight

plt.tight_layout()
plt.savefig('kayanuma_comparison.png')
