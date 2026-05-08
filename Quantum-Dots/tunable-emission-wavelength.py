import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34      # Planck's constant (JÂ·s)
e = 1.602e-19      # Elementary charge (C)
m_0 = 9.109e-31    # Electron rest mass (kg)
eps_0 = 8.854e-12  # Vacuum permittivity (F/m)

def brus_equation(R_nm, Eg_ev, epsilon, me_eff, mh_eff):
    R = R_nm * 1e-9  # nm to meters
    
    # Term 1: Kinetic Confinement Energy
    # (h^2 / 8R^2) * (1/me + 1/mh)
    confinement = (h**2 / (8 * R**2)) * (1/(me_eff * m_0) + 1/(mh_eff * m_0))
    
    # Term 2: Coulomb Attraction Energy
    # (1.8 * e^2) / (4 * pi * eps_0 * eps * R)
    coulomb = (1.8 * e**2) / (4 * np.pi * eps_0 * epsilon * R)
    
    E_total_j = (Eg_ev * e) + confinement - coulomb
    E_ev = E_total_j / e
    
    # Convert Energy to Wavelength (nm)
    wavelength_nm = 1240 / E_ev
    return E_ev, wavelength_nm

# Material data
materials = {
    'CdSe': {'Eg': 1.74, 'eps': 10.6, 'me': 0.13, 'mh': 0.45},
    'CdS':  {'Eg': 2.42, 'eps': 5.7,  'me': 0.21, 'mh': 0.80},
    'ZnSe': {'Eg': 2.70, 'eps': 9.1,  'me': 0.17, 'mh': 0.60},
    'ZnS':  {'Eg': 3.68, 'eps': 8.3,  'me': 0.34, 'mh': 0.23}
}

radii = np.linspace(1.2, 7.0, 100) # nm
plt.figure(figsize=(10, 6))

for name, p in materials.items():
    res = [brus_equation(r, p['Eg'], p['eps'], p['me'], p['mh']) for r in radii]
    wavelengths = [r[1] for r in res]
    
    plt.plot(radii, wavelengths, label=name, linewidth=2.5)

# Visual Aesthetics
plt.title('Brus Equation: Size-Tunable Emission Wavelength', fontsize=14)
plt.xlabel('Quantum Dot Radius (nm)', fontsize=12)
plt.ylabel('Emission Wavelength (nm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Material")

# Add a rainbow gradient background to represent the visible spectrum
plt.axhspan(400, 700, color='lightgray', alpha=0.2, label='Visible Range')
plt.text(6, 420, 'Visible Spectrum', color='gray', fontsize=10)

plt.ylim(200, 800)
plt.tight_layout()
plt.show()
