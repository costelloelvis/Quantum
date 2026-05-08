import numpy as np
from scipy.constants import hbar, m_e

def confinement_energy(R, m_eff_e, m_eff_h):
    """
    Calculates the first-order confinement energy.
    R: radius of the dot in meters
    m_eff_e: effective mass of electron (as a multiple of m_e)
    m_eff_h: effective mass of hole (as a multiple of m_e)
    """
    reduced_mass = (m_eff_e * m_eff_h) / (m_eff_e + m_eff_h) * m_e
    return (hbar**2 * np.pi**2) / (2 * reduced_mass * R**2)