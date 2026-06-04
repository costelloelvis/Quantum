# Quantum Computing & Quantum Physics Portfolio

A collection of quantum computing, quantum information, and semiconductor quantum physics projects implemented in Python.

This repository serves as a research and educational portfolio showcasing simulations, algorithms, and computational models that connect theoretical quantum mechanics with practical quantum programming and numerical analysis.

---

## Overview

The repository is organized into three major project areas:

### Quantum Demo

Interactive and experimental simulations designed to visualize and explore quantum phenomena.

#### Features

* Quantum system visualization
* Interactive simulations using Streamlit
* Numerical experiments and benchmarking
* Educational demonstrations of quantum behavior
* Public outreach and academic showcase projects

---

### Quantum Dots

A collection of semiconductor quantum-dot simulations focused on nanoscale electronic and optical properties.

#### Research Topics

* Size-dependent photoluminescence
* Quantum confinement effects
* Quantum Confined Stark Effect (QCSE)
* Auger recombination decay
* Coulomb interaction modeling
* Semiconductor nanocrystal physics

#### Implemented Models

* Brus Equation
* Kayanuma Corrections
* Exciton energy calculations
* Emission wavelength prediction

---

### Quantum Algorithms & Information

Implementations of foundational quantum computing algorithms and communication protocols.

#### Quantum Protocols

* BB84 Quantum Key Distribution (QKD)
* Quantum Teleportation
* Basic quantum cryptography demonstrations

#### Quantum Algorithms

* Grover's Search Algorithm
* Educational implementation of Shor's Algorithm
* Quantum circuit construction
* Statevector simulations

#### Quantum Gates & Circuits

* Hadamard Gate
* Pauli Gates
* Controlled-NOT (CNOT)
* Multi-qubit operations
* Bloch sphere visualizations
* Noise and error-model experiments

---

## Scientific Motivation

This repository explores how quantum mechanical principles can be transformed into computational models and executable simulations.

Key goals include:

* Understanding quantum information processing
* Modeling nanoscale semiconductor systems
* Investigating quantum communication protocols
* Developing numerical solutions to quantum mechanical problems
* Building practical quantum programming experience

---

## Technologies

### Programming Language

* Python 3

### Scientific Computing

* NumPy
* SciPy
* Matplotlib

### Quantum Computing

* Qiskit
* QuTiP

### Interactive Applications

* Streamlit

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/costelloelvis/Quantum.git
cd Quantum
```

### Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install numpy scipy matplotlib qutip qiskit streamlit
```

Or:

```bash
pip install -r requirements.txt
```

---

## Running Projects

### Interactive Quantum Simulations

```bash
streamlit run Quantum-Demo/qds.py
```

### Quantum Dot Simulations

```bash
python Quantum-Dots/energyplot.py
```

### Quantum Computing Scripts

```bash
python Personal/grover.py
python Personal/bb84.py
python Personal/teleportation.py
```

---

## Research Themes

### Semiconductor Quantum Physics

* Quantum confinement
* Excitonic effects
* Nanostructure optics
* Electronic transition energies

### Quantum Information Science

* Quantum cryptography
* Quantum communication
* Quantum algorithms
* Quantum error modeling

### Computational Physics

* Numerical simulation
* Scientific visualization
* Quantum system dynamics
* Reproducible scientific computing

---

## Future Development

* [ ] IBM Quantum backend integration using Qiskit Runtime
* [ ] Variational Quantum Eigensolver (VQE)
* [ ] Quantum Machine Learning experiments
* [ ] Interactive Jupyter notebooks
* [ ] Advanced Bloch sphere visualizations
* [ ] OpenQASM 3 support
* [ ] Quantum error correction demonstrations
* [ ] Unified simulation framework

---

## Academic Applications

This repository is intended for:

* Physics students
* Computational physics learners
* Quantum computing enthusiasts
* Undergraduate research projects
* Graduate-school portfolio preparation
* Quantum information science exploration

---

## Author

### Elvis Wanjiru

Physics • Computational Physics • Quantum Computing

Areas of Interest:

* Quantum Information Science
* Semiconductor Physics
* Computational Physics
* Scientific Programming
* Numerical Simulation

GitHub: https://github.com/costelloelvis

---

## License

This project is available for educational, research, and non-commercial use.

Contributions, feedback, and collaborations are welcome.
