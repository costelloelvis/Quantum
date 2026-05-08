import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --- Constants ---
H = 6.626e-34
HBAR = H / (2 * np.pi)
C = 3.0e8
E_CHARGE = 1.602e-19
M_0 = 9.11e-31
EPS0 = 8.854e-12

# --- Materials (added Varshni params: alpha, beta) ---
materials = {
    "CdSe": {"Eg": 1.74, "me": 0.13, "mh": 0.45, "epsilon": 10.6, "alpha": 4.9e-4, "beta": 245},
    "ZnS":  {"Eg": 3.68, "me": 0.34, "mh": 0.23, "epsilon": 8.9,  "alpha": 5.0e-4, "beta": 300},
    "InP":  {"Eg": 1.34, "me": 0.07, "mh": 0.60, "epsilon": 12.5, "alpha": 4.5e-4, "beta": 200},
    "CdS":  {"Eg": 2.42, "me": 0.21, "mh": 0.80, "epsilon": 9.1,  "alpha": 3.5e-4, "beta": 180},
    "GaAs": {"Eg": 1.42, "me": 0.067,"mh": 0.50, "epsilon": 12.9, "alpha": 5.4e-4, "beta": 204},
    "PbS":  {"Eg": 0.41, "me": 0.08, "mh": 0.08, "epsilon": 169.0,"alpha": 4e-4,   "beta": 150},
}

st.set_page_config(page_title="Quantum Dot Research Simulator", layout="wide")

st.title("⚛️ Advanced Quantum Dot Simulator (Research Grade)")

# --- Sidebar ---
st.sidebar.header("Controls")
material = st.sidebar.selectbox("Material", list(materials.keys()))
R_nm = st.sidebar.slider("Dot Radius (nm)", 0.5, 12.0, 3.0)
T = st.sidebar.slider("Temperature (K)", 50, 500, 300)

# --- Physics Functions ---
def varshni_bandgap(Eg0, alpha, beta, T):
    return Eg0 - (alpha * T**2) / (T + beta)

def exciton_bohr_radius(me, mh, epsilon_r):
    mu = (me * mh) / (me + mh)
    return (4 * np.pi * EPS0 * epsilon_r * HBAR**2) / (mu * E_CHARGE**2)

def kayanuma_energy(mat, R_nm, T):
    R = R_nm * 1e-9

    Eg_T = varshni_bandgap(mat["Eg"], mat["alpha"], mat["beta"], T) * E_CHARGE

    me = mat["me"] * M_0
    mh = mat["mh"] * M_0
    epsilon = mat["epsilon"] * EPS0

    # Confinement
    confinement = (HBAR**2 * np.pi**2 / (2 * R**2)) * ((1/me) + (1/mh))

    # Coulomb
    coulomb = 1.786 * (E_CHARGE**2) / (4 * np.pi * epsilon * R)

    # --- Dielectric mismatch (image charge correction) ---
    # assuming surrounding medium ~ air (ε_out ≈ 1)
    epsilon_in = mat["epsilon"]
    epsilon_out = 1.0
    polarization = (0.124 * E_CHARGE**2 / (4 * np.pi * EPS0 * R)) * ((epsilon_in - epsilon_out)/(epsilon_in + epsilon_out))

    # Exciton Rydberg
    mu = (me * mh) / (me + mh)
    ER = (mu * E_CHARGE**4) / (2 * (4 * np.pi * epsilon)**2 * HBAR**2)

    correlation = 0.248 * ER

    E = Eg_T + confinement - coulomb - correlation + polarization

    wl_nm = (H * C / E) * 1e9

    return E / E_CHARGE, wl_nm

# --- Calculate ---
mat = materials[material]
energy_ev, abs_wl = kayanuma_energy(mat, R_nm, T)

# --- Exciton properties ---
aB = exciton_bohr_radius(mat["me"]*M_0, mat["mh"]*M_0, mat["epsilon"]) * 1e9
regime = "Strong Confinement" if R_nm < aB else "Weak Confinement"

# --- Stokes shift ---
stokes_shift = 20 / R_nm
em_wl = abs_wl + stokes_shift

# --- Oscillator strength ---
osc = 1 / (R_nm**3)

# --- Metrics ---
col1, col2, col3 = st.columns(3)

col1.metric("Absorption (nm)", f"{abs_wl:.2f}")
col2.metric("Emission (nm)", f"{em_wl:.2f}")
col3.metric("Bandgap (eV)", f"{energy_ev:.3f}")

st.info(f"""
Bohr Radius: {aB:.2f} nm  
Regime: {regime}  
Oscillator Strength ~ {osc:.3e}
""")

# --- Tabs ---
tabs = st.tabs(["📊 Spectra", "🌀 Wavefunction", "🌊 Time-Resolved PL", "🧠 Theory"])

# --- Spectra ---
with tabs[0]:
    x = np.linspace(200, 1200, 2000)
    sigma = 25

    absorption = np.exp(-0.5*((x - abs_wl)/sigma)**2)
    emission = np.exp(-0.5*((x - em_wl)/sigma)**2)

    fig, ax = plt.subplots()
    ax.plot(x, absorption, '--', label="Absorption")
    ax.plot(x, emission, label="Emission")

    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')
    ax.tick_params(colors='white')
    ax.set_xlabel("Wavelength (nm)", color='white')
    ax.set_ylabel("Intensity", color='white')
    ax.legend()

    st.pyplot(fig)

# --- Wavefunction ---
with tabs[1]:
    res = 25
    grid = np.linspace(-R_nm, R_nm, res)
    x, y, z = np.meshgrid(grid, grid, grid)
    r = np.sqrt(x**2 + y**2 + z**2)

    psi_sq = np.where(r <= R_nm, (np.sin(np.pi*r/R_nm)/r)**2, 0)
    psi_sq[r == 0] = (np.pi/R_nm)**2

    fig = go.Figure(data=go.Volume(
        x=x.flatten(), y=y.flatten(), z=z.flatten(),
        value=psi_sq.flatten(),
        opacity=0.1,
        surface_count=12
    ))

    st.plotly_chart(fig, use_container_width=True)

# --- Time-Resolved PL ---
with tabs[2]:
    st.write("Photoluminescence decay (Exciton recombination)")

    t = np.linspace(0, 50, 500)  # ns
    tau = 10 * (R_nm/3)**3  # lifetime scaling

    decay = np.exp(-t / tau)

    fig, ax = plt.subplots()
    ax.plot(t, decay)

    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Intensity")
    ax.set_title(f"Lifetime τ ≈ {tau:.2f} ns")

    st.pyplot(fig)

# --- Theory ---
with tabs[3]:
    st.latex(r"E(T) = E_0 - \frac{\alpha T^2}{T + \beta}")
    st.write("Varshni equation: bandgap shrinks with temperature")

    st.write("Kayanuma equation includes confinement, Coulomb, and correlation effects")

    st.write(f"Current regime: {regime}")