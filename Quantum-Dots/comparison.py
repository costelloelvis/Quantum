import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, e, m_e

# Material database
materials = {
    "CdSe": {"Eg": 1.74, "me": 0.13, "mh": 0.45},
    "ZnS":  {"Eg": 3.68, "me": 0.34, "mh": 1.76},
    "InP":  {"Eg": 1.35, "me": 0.07, "mh": 0.60}
}

radii = np.linspace(1e-9, 6e-9, 100)  # 1nm to 6nm

plt.figure(figsize=(10, 6))

for name, params in materials.items():
    Eg_joules = params["Eg"] * e
    # Reduced mass calculation
    mu = (params["me"] * params["mh"]) / (params["me"] + params["mh"]) * m_e
    
    # Simple Brus Equation (Kinetic term only for demonstration)
    E_total = params["Eg"] + (h**2 / (8 * mu * radii**2 * e))
    
    plt.plot(radii * 1e9, E_total, label=f"{name}")

plt.xlabel("Radius (nm)")
plt.ylabel("Emission Energy (eV)")
plt.title("Size-Dependent Energy Shift for Various Semiconductors")
plt.legend()
plt.grid(True)
plt.show()