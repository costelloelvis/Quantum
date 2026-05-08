import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --- Physical Constants ---
H_BAR = 1.054e-34    # Reduced Planck's constant (J*s)
H = 6.626e-34
C = 3.0e8
E_CHARGE = 1.602e-19
EPSILON_0 = 8.854e-12
M_0 = 9.11e-31

# --- Expanded Materials Dictionary ---
materials = {
    "CdSe (Cadmium Selenide)": {"Eg": 1.74, "me": 0.13, "mh": 0.45, "epsilon": 10.6},
    "ZnS (Zinc Sulfide)":      {"Eg": 3.68, "me": 0.34, "mh": 0.23, "epsilon": 8.9},
    "InP (Indium Phosphide)":  {"Eg": 1.34, "me": 0.07, "mh": 0.60, "epsilon": 12.5},
    "CdS (Cadmium Sulfide)":   {"Eg": 2.42, "me": 0.21, "mh": 0.80, "epsilon": 9.1},
    "GaAs (Gallium Arsenide)": {"Eg": 1.42, "me": 0.067, "mh": 0.50, "epsilon": 12.9},
    "PbS (Lead Sulfide)":      {"Eg": 0.41, "me": 0.08, "mh": 0.08, "epsilon": 169.0},
}

st.set_page_config(page_title="Quantum Dot Simulator", layout="wide")

st.title("⚛️Quantum Dot Simulator (Kayanuma Model)")
st.markdown("Exploring the full optical spectrum from **Ultraviolet** to **Infrared** via size-tuning.")

# --- Sidebar ---
st.sidebar.header("Control Parameters")
selected_name = st.sidebar.selectbox("Semiconductor Material", list(materials.keys()))
radius_nm = st.sidebar.slider("Dot Radius (nm)", 0.5, 15.0, 4.0, step=0.1)

# --- Physics Engine: Kayanuma Logic ---
def calculate_kayanuma(material_name, R_nm):
    mat = materials[material_name]
    R = R_nm * 1e-9
    Eg_bulk = mat["Eg"] * E_CHARGE
    me_eff, mh_eff = mat["me"] * M_0, mat["mh"] * M_0
    mu = (me_eff * mh_eff) / (me_eff + mh_eff)
    epsilon = mat["epsilon"] * EPSILON_0

    # 1. Confinement Term (Kinetic Energy)
    E_conf = (H_BAR**2 * np.pi**2) / (2 * mu * R**2)

    # 2. Coulomb Term (Attractive)
    E_coul = (1.786 * E_CHARGE**2) / (4 * np.pi * epsilon * R)

    # 3. Correlation Term (Rydberg Correction)
    E_ry_star = (mu * E_CHARGE**4) / (2 * H_BAR**2 * (4 * np.pi * epsilon)**2)
    E_corr = 0.248 * E_ry_star

    Eqd_joules = Eg_bulk + E_conf - E_coul - E_corr
    wl_nm = (H * C / Eqd_joules) * 1e9
    return Eqd_joules / E_CHARGE, wl_nm

energy_ev, peak_wl = calculate_kayanuma(selected_name, radius_nm)

# --- Expanded Application Logic ---
def get_extended_suggestion(wl):
    if wl < 300:
        return "☢️ **Deep UV:** Applications in high-resolution lithography and advanced chemical sensing."
    elif 300 <= wl < 400:
        return "🛡️ **UV-A/B:** Ideal for sterilization (UV-C LEDs), forensic analysis, and counterfeit detection."
    elif 400 <= wl < 700:
        return "🌈 **Visible Light:** Perfect for QLED displays (Red/Green/Blue) and cellular bio-tagging."
    elif 700 <= wl < 1400:
        return "📡 **Near-Infrared (NIR):** Used in deep-tissue medical imaging, night vision, and LIDAR for autonomous vehicles."
    elif 1400 <= wl < 3000:
        return "🌐 **Short-Wave IR (SWIR):** Critical for fiber-optic telecommunications and moisture-sensing in agriculture."
    else:
        return "🛰️ **Mid-IR / Thermal:** Applications in thermal imaging, gas leak detection, and astronomy."

suggestion = get_extended_suggestion(peak_wl)

# --- UI Layout ---
col_m, col_s = st.columns([1, 2])
with col_m:
    st.metric("Emission Peak", f"{peak_wl:.2f} nm")
    st.metric("Quantum Gap", f"{energy_ev:.3f} eV")
with col_s:
    st.info(f"**Application Insight:**\n\n{suggestion}")

tabs = st.tabs(["📊 Spectral Analysis", "🌀 3D Confinement", "📚 Kayanuma Theory"])

with tabs[0]:
    x = np.linspace(min(200, peak_wl-100), max(2000, peak_wl+100), 1500)
    y = np.exp(-0.5 * ((x - peak_wl) / 20)**2)
    fig_pl, ax = plt.subplots(figsize=(10, 4), facecolor='#0e1117')
    ax.set_facecolor('#0e1117')
    ax.plot(x, y, color='#00FFAA', lw=3)
    ax.fill_between(x, y, color='#00FFAA', alpha=0.2)
    ax.axvline(peak_wl, color='red', linestyle='--', label=f'Peak: {peak_wl:.1f}nm')
    ax.tick_params(colors='white')
    ax.set_xlabel("Wavelength (nm)", color='white')
    st.pyplot(fig_pl)

with tabs[1]:
    st.write("Electron-Hole Pair spatial distribution (Ground State)")
    res = 20
    limit = radius_nm * 1.2
    grid = np.linspace(-limit, limit, res)
    X, Y, Z = np.meshgrid(grid, grid, grid)
    R_dist = np.sqrt(X**2 + Y**2 + Z**2)
    psi_sq = np.where(R_dist <= radius_nm, (np.sin(np.pi * R_dist / radius_nm) / R_dist)**2, 0)
    psi_sq[R_dist == 0] = (np.pi / radius_nm)**2

    fig_3d = go.Figure(data=go.Volume(
        x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
        value=psi_sq.flatten(), isomin=0.1*psi_sq.max(), isomax=psi_sq.max(),
        opacity=0.1, surface_count=10, colorscale='Electric'
    ))
    fig_3d.update_layout(scene=dict(xaxis_title='x (nm)', yaxis_title='y (nm)', zaxis_title='z (nm)'), margin=dict(l=0, r=0, b=0, t=0))
    st.plotly_chart(fig_3d, use_container_width=True)

with tabs[2]:
    st.subheader("The Kayanuma Correction")
    st.write("Unlike the basic Brus model, the Kayanuma equation accounts for electron-hole correlation.")
    st.latex(r"E_{total} = E_g + \frac{\hbar^2 \pi^2}{2 \mu R^2} - \frac{1.786 e^2}{4 \pi \epsilon_0 \epsilon_r R} - 0.248 E_{Ry}^*")
    st.markdown("""
    * **The First Correction ($1/R$):** Accounts for the Coulombic attraction between the electron and the hole.
    * **The Second Correction ($E_{Ry}^*$):** Is a constant energy shift independent of $R$ that accounts for the spatial correlation between the particles.
    """)