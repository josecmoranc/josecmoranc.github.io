# Numerical codes
Numerical codes for measurements, post-processing experimental data, and different numerical simulations are provided. The latter include population balance simulations of aerosol coagulation, aerosol particle charging, fractal-like agglomerates, Monte Carlo DEM simulations, and Langevin Dynamics

## 1. Computational simulations

* **FracVAL:** (old version Fortran, new version C++/Python) Software to generate 3d off-lattice agglomerates of nanoparticles. The original Fortran code is available in [Computer Physics Communications](https://doi.org/10.1016/j.cpc.2019.01.015).  A new version of FracVAL combining C++/Python with a [GitLab repository](https://gitlab.com/jmoranc1/fracval_cpp), and extending its capabilities is currently being developed.

* **MCAC:** (C++/Python) This is a Monte Carlo DEM software to simulate the nucleation, agglomeration, surface growth, and oxidation of aerosol particles. The code has been particularly adapted to take thermodynamic and fluid properties from CFD simulations under flame conditions. This code is available through [CORIA-CFD GitLab](https://gitlab.coria-cfd.fr/MCAC/MCAC/).

* **NGDE-cpp:** (C++/Python) A nodal Population Balance code to simulate the dynamics of aerosol or colloid suspensions experiencing coagulation. This code is available though the following [GitLab repository](https://gitlab.com/jmoranc1/ngde_cpp).
    
* **FTP-cpp:** (C++/Python) This is a Langevin Dynamics code to simulate the dynamics of suspended nanoparticles and determine their collision rates based on a first-time-passage approach. This code is available thgough the following [GitLab repository](https://gitlab.com/jmoranc1/ftp_kernels_langevin_dynamics).

* **LBM-PLF:** (C++/Python) A Lattice-Boltzmann coupled with DEM for simulating particle-laden flows is being developed. Currently in a private GitLab repository.

* **Aerosol particle charging:** (Python) This is a population balance model for particle charging through 2 mechanisms namely diffusion and field charging. The model also considers the particle electrophoretic deposition in an electrostatic precipitator (ESP). This code is available through [this GitHub repository](https://github.com/Aerosol-Lab/Aerosol_particle_charging_1d_model).

## 2. Experimental measurements
* **TDMA measurements:** This code allows controlling 2 DMA's (differential mobility analyzer), their respective HV (high-voltage) units, and a CPC (condensation particle counter) for conducting TDMA (tandem DMA) measurements. This code includes GUI to introduce parameters and run the experiments. This code is available through the following [GitHub repository](https://github.com/Aerosol-Lab/TDMA_measurements).

## 3. Post-processing experimental data
