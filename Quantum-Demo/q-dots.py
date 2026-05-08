import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --- Physical Constants ---
H = 6.626e-34      # Planck's constant (J*s)
C = 3.0e8          # Speed of light (m/s)
E_CHARGE = 1.602e-19
M_0 = 9.11e-31     # Electron rest mass (kg)

# --- Expanded Materials Dictionary ---
# Data includes Bulk Bandgap (eV), Effective masses (me, mh), and Dielectric constant
materials = {
    "CdSe (Cadmium Selenide)": {"Eg": 1.74, "me": 0.13, "mh": 0.45, "epsilon": 10.6},
    "ZnS (Zinc Sulfide)":      {"Eg": 3.68, "me": 0.34, "mh": 0.23, "epsilon": 8.9},
    "InP (Indium Phosphide)":  {"Eg": 1.34, "me": 0.07, "mh": 0.60, "epsilon": 12.5},
    "CdS (Cadmium Sulfide)":   {"Eg": 2.42, "me": 0.21, "mh": 0.80, "epsilon": 9.1},
    "GaAs (Gallium Arsenide)": {"Eg": 1.42, "me": 0.067, "mh": 0.50, "epsilon": 12.9},
    "PbS (Lead Sulfide)":      {"Eg": 0.41, "me": 0.08, "mh": 0.08, "epsilon": 169.0},
}

st.set_page_config(page_title="Quantum Dot Simulator", layout="wide")

# --- UI Header ---
st.title("⚛️ Quantum Dot PL & Wavefunction Simulator")
st.markdown("""
Predicting **Size-Dependent Photoluminescence** and **Spatial Confinement** using the 
Brus Equation (Effective Mass Approximation).
""")

# --- Sidebar Inputs ---
st.sidebar.header("Control Parameters")
selected_name = st.sidebar.selectbox("Semiconductor Material", list(materials.keys()))
radius_nm = st.sidebar.slider("Dot Radius (nm)", 0.5, 12.0, 3.5, step=0.1)

# --- Physics Engine ---
def calculate_physics(material_name, R_nm):
    mat = materials[material_name]
    R = R_nm * 1e-9
    Eg_bulk = mat["Eg"] * E_CHARGE
    me_eff, mh_eff = mat["me"] * M_0, mat["mh"] * M_0
    
    # Brus Equation: E_qd = E_bulk + Confinement - Coulomb (Coulomb is small, often neglected in simple models)
    reduced_mass = (1/me_eff) + (1/mh_eff)
    confinement = (H**2 * reduced_mass) / (8 * R**2)
    
    Eqd_joules = Eg_bulk + confinement
    wl_nm = (H * C / Eqd_joules) * 1e9
    return Eqd_joules / E_CHARGE, wl_nm

energy_ev, peak_wl = calculate_physics(selected_name, radius_nm)

# --- Device Suggestion Logic ---
def get_suggestion(wl):
    if 380 <= wl < 450:
        return "💜 UV/Violet: Ideal for high-density optical storage or sterilization tools."
    elif 450 <= wl < 495:
        return "💙 Blue: Optimal for high-efficiency Blue LEDs and backlit displays."
    elif 495 <= wl < 570:
        return "💚 Green: Optimal for Bio-imaging markers and fluorescent tagging."
    elif 570 <= wl < 620:
        return "💛 Yellow/Orange: Ideal for specialized signaling and warm-spectrum lighting."
    elif 620 <= wl < 750:
        return "❤️ Deep Red: Ideal for QLED Displays and medical therapy lasers."
    elif wl >= 750:
        return "🔦 Infrared: Suitable for night-vision sensors or telecommunications."
    else:
        return "⚠️ Outside Visible Range: Check radius parameters for target application."

suggestion = get_suggestion(peak_wl)

# --- Main Layout ---
col_metrics, col_suggest = st.columns([1, 2])
with col_metrics:
    st.metric("Peak Wavelength", f"{peak_wl:.2f} nm")
    st.metric("Quantum Bandgap", f"{energy_ev:.3f} eV")

with col_suggest:
    st.success(f"**Device Application Suggestion:**\n\n{suggestion}")

# --- Tabs for Visuals ---
tabs = st.tabs(["📊 PL Spectrum", "🌀 3D Wavefunction Density", "📝 Theory"])

with tabs[0]:
    x_spec = np.linspace(200, 1000, 1000)
    # Gaussian broadening to simulate a real ensemble
    y_spec = np.exp(-0.5 * ((x_spec - peak_wl) / 15)**2)
    
    fig_spec, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x_spec, y_spec, color='cyan', lw=3)
    ax.fill_between(x_spec, y_spec, color='cyan', alpha=0.2)
    ax.axvline(peak_wl, color='red', linestyle='--', alpha=0.6)
    
    # Dark mode styling for a sleek dashboard
    ax.set_facecolor('#0e1117')
    fig_spec.patch.set_facecolor('#0e1117')
    ax.tick_params(colors='white')
    ax.set_xlabel("Wavelength (nm)", color='white')
    ax.set_ylabel("Normalized Intensity", color='white')
    st.pyplot(fig_spec)

with tabs[1]:
    st.write("Visualizing the Ground State Electron Probability Density $|\psi|^2$")
    res = 25
    limit = radius_nm * 1.2
    grid = np.linspace(-limit, limit, res)
    x, y, z = np.meshgrid(grid, grid, grid)
    r = np.sqrt(x**2 + y**2 + z**2)
    
    # Radial part of the wavefunction for an infinite spherical well (first Bessel function)
    # psi ~ sin(pi*r/R) / r
    psi_sq = np.where(r <= radius_nm, (np.sin(np.pi * r / radius_nm) / r)**2, 0)
    psi_sq[r == 0] = (np.pi / radius_nm)**2 

    fig_3d = go.Figure(data=go.Volume(
        x=x.flatten(), y=y.flatten(), z=z.flatten(),
        value=psi_sq.flatten(),
        isomin=0.05 * psi_sq.max(), isomax=psi_sq.max(),
        opacity=0.1, surface_count=12,
        colorscale='Plasma'
    ))
    
    fig_3d.update_layout(scene=dict(xaxis_title='X (nm)', yaxis_title='Y (nm)', zaxis_title='Z (nm)'),
                        margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_3d, use_container_width=True)

with tabs[2]:
    st.markdown("### The Physics of Confinement")
    st.latex(r"E_{QD} = E_g + \frac{h^2}{8R^2} \left( \frac{1}{m_e^*} + \frac{1}{m_h^*} \right)")
    st.write("""
    The tool calculates the blue-shift in the bandgap as the nanocrystal radius $R$ 
    decreases. This occurs because the carriers (electrons and holes) are confined 
    spatially, increasing their kinetic energy—much like a particle in a box. 
    
    **Parameters used:**
    - Planck's Constant ($h$)
    - Effective mass of Electron ($m_e^*$)
    - Effective mass of Hole ($m_h^*$)
    """)