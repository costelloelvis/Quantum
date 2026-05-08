import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Physical Constants ---
H = 6.626e-34      # Planck's constant (J*s)
C = 3.0e8          # Speed of light (m/s)
E_CHARGE = 1.602e-19
M_0 = 9.11e-31     # Electron rest mass (kg)

# Material Parameters (Example: CdSe)
materials = {
    "CdSe": {"Eg": 1.74, "me": 0.13, "mh": 0.45, "epsilon": 10.6},
    "ZnS":  {"Eg": 3.68, "me": 0.34, "mh": 0.23, "epsilon": 8.9},
    "InP":  {"Eg": 1.34, "me": 0.07, "mh": 0.60, "epsilon": 12.5}
}

st.set_page_config(page_title="Quantum Dot Simulator", layout="wide")

st.title("⚛️ Quantum Dot PL Simulator")
st.markdown("""
Predict the **Size-Dependent Photoluminescence** of semiconductor nanocrystals 
using the Brus Equation (Effective Mass Approximation).
""")

# --- Sidebar Inputs ---
st.sidebar.header("Control Parameters")
selected_material = st.sidebar.selectbox("Semiconductor Material", list(materials.keys()))
radius_nm = st.sidebar.slider("Dot Radius (nm)", 1.0, 10.0, 3.5, step=0.1)

# --- The Physics Engine ---
def calculate_pl(material_name, R_nm):
    mat = materials[material_name]
    R = R_nm * 1e-9  # Convert to meters
    
    # 1. Bulk Bandgap (J)
    Eg_bulk = mat["Eg"] * E_CHARGE
    
    # 2. Confinement Term
    me_eff = mat["me"] * M_0
    mh_eff = mat["mh"] * M_0
    reduced_mass = (1/me_eff) + (1/mh_eff)
    confinement = (H**2 * reduced_mass) / (8 * R**2)
    
    # 3. Total Energy Gap (Joules)
    Eqd_joules = Eg_bulk + confinement
    Eqd_ev = Eqd_joules / E_CHARGE
    
    # 4. Wavelength (nm)
    wavelength_nm = (H * C / Eqd_joules) * 1e9
    return Eqd_ev, wavelength_nm

# Run Calculations
energy_ev, peak_wl = calculate_pl(selected_material, radius_nm)

# --- Visualization ---
col1, col2 = st.columns([1, 1])

with col1:
    st.metric("Peak Emission Wavelength", f"{peak_wl:.2f} nm")
    st.metric("Quantum Energy Gap", f"{energy_ev:.3f} eV")

    # Generate PL Spectrum Curve (Gaussian)
    x = np.linspace(300, 900, 1000)
    sigma = 15  # Spectral broadening
    y = np.exp(-0.5 * ((x - peak_wl) / sigma)**2)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color='cyan', lw=3)
    ax.fill_between(x, y, color='cyan', alpha=0.2)
    ax.axvline(peak_wl, color='red', linestyle='--', label=f'Peak: {peak_wl:.1f}nm')
    
    ax.set_facecolor('#1e1e1e')
    fig.patch.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Intensity (a.u.)")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Theoretical Framework")
    st.latex(r"E_{QD} = E_g + \frac{h^2}{8R^2} \left( \frac{1}{m_e^*} + \frac{1}{m_h^*} \right)")
    st.info(f"""
    **Current Configuration:**
    - **Material:** {selected_material}
    - **Confinement Regime:** Strong (R < Exciton Bohr Radius)
    - **Application:** Optimized for light-emitting diodes (LEDs).
    """)