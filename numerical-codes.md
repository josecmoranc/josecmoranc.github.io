# Numerical codes
Numerical codes for measurements, post-processing experimental data, and different numerical simulations are provided. The latter include population balance simulations of aerosol coagulation, aerosol particle charging, fractal-like agglomerates, Monte Carlo DEM simulations, and Langevin Dynamics

## 1. Computational simulations

* **FracVAL:** (old version Fortran, new version C++/Python) Software to generate 3d off-lattice agglomerates of particles. The code use a particle-cluster agglomeration approach to generate a initial population of small clusters. Subsequently, uses a quasi-hierarchical cluster-cluster aggregation approach where fractal parameters are retained constant all along the generation process (see the figure below for an example). The original Fortran code is available in [Computer Physics Communications](https://doi.org/10.1016/j.cpc.2019.01.015). A user manual is [available here](https://doi.org/10.13140/RG.2.2.17240.32007).  A new version of FracVAL combining C++/Python with a [GitLab repository](https://gitlab.com/jmoranc1/fracval_cpp), and extending its capabilities is currently being developed.
[![Figure02](https://user-images.githubusercontent.com/62391931/235360986-4cb3dbbd-bed3-4089-9630-d4fc0001f6e7.png)](https://doi.org/10.1016/j.cpc.2019.01.015)

* **MCAC:** (C++/Python) This is a Monte Carlo DEM software to simulate the nucleation, agglomeration, surface growth, and oxidation of aerosol particles. The code has been particularly adapted to take thermodynamic and fluid properties from CFD simulations under flame conditions (see the figure below). This code is available through [CORIA-CFD GitLab](https://gitlab.coria-cfd.fr/MCAC/MCAC/).
[![Screenshot from 2023-04-30 10-28-29](https://user-images.githubusercontent.com/62391931/235361648-5c7a82ad-b264-4d7c-b86a-670b08e40b66.png)](https://gitlab.coria-cfd.fr/MCAC/MCAC/)

* **NGDE-cpp:** (C++/Python) A nodal Population Balance code to simulate the dynamics of aerosol or colloid suspensions experiencing coagulation is carried out. The nodes are used to discretize the particle size distribution which can span several decades in size. Here we solve the population balance equation and consider all the collision rates between nodes determined by their collision kernels (see the figure below). This code is available though the following [GitLab repository](https://gitlab.com/jmoranc1/ngde_cpp).
[![Screenshot from 2023-04-30 10-25-58](https://user-images.githubusercontent.com/62391931/235361533-30628d94-ef93-483d-b110-51a24c75d7f3.png)](https://gitlab.com/jmoranc1/ngde_cpp)
    
* **FTP-cpp:** (C++/Python) This is a Langevin Dynamics code to simulate the dynamics of suspended nanoparticles and determine their collision rates based on a first-time-passage approach. Here the Langevin equation is solved to determine the trajectories of aerosol particles suspended in still gas and determining their collision kernels. This code is available thgough the following [GitLab repository](https://gitlab.com/jmoranc1/ftp_kernels_langevin_dynamics).
[![FTP](https://user-images.githubusercontent.com/62391931/235362135-4580e749-24d1-48a8-bf01-5dd145164257.png)](https://gitlab.com/jmoranc1/ftp_kernels_langevin_dynamics)

* **Aerosol particle charging:** (Python) This is a population balance model for particle charging through 2 mechanisms namely diffusion and field charging. The model also considers the particle electrophoretic deposition in an electrostatic precipitator (ESP). This code is available through [this GitHub repository](https://github.com/Aerosol-Lab/Aerosol_particle_charging_1d_model).
[![Charging-1d](https://user-images.githubusercontent.com/62391931/229414629-e120c1b8-9bfe-4ec6-8656-5deb0bda6ed0.png)](https://github.com/Aerosol-Lab/Aerosol_particle_charging_1d_model)

* **LBM-PLF:** (C++/Python) A Lattice-Boltzmann coupled with DEM for simulating particle-laden flows is being developed. Currently in a private GitLab repository but will be available here in the future.

## 2. Post-processing experimental data
* **Onedimensional DMA:** (Python) This code is used for post-processing (deconvolution) 1d single differential mobility analyzer (DMA) scan measurements for particle sizng. This code is available through the following  [GitHub repository](https://github.com/Aerosol-Lab/OneDimensional_DMA_inversion).

* **Bidimensional TDMA:** (Python) This code is used for post-processing (deconvolution) 2d tandem differential mobility analyzer (TDMA) measurements of nanoparticle size and electric charge distributions. This code is available through the following  [GitHub repository](https://github.com/Aerosol-Lab/Bidimensional_TDMA_inversion).

* **Bidimensional DMA-APS:** (Python) This code is used for post-processing (deconvolution) 2d differential mobility analyzer (DMA) in tandem configuration with an aerodynamic particle spectrometer (APS) measurements of micrometer sized aerosol particle size and electric charge distributions. This code is available through the following  [GitHub repository](https://github.com/Aerosol-Lab/Bidimensional_DMA_APS_inversion).

## 3. Experimental measurements
* **TDMA measurements:** (Python) This code allows controlling 2 DMA's (differential mobility analyzer), their respective HV (high-voltage) units, and a CPC (condensation particle counter) for conducting TDMA (tandem DMA) measurements. This code includes GUI (see the picture below) to introduce parameters and run the experiments. This code is available through the following [GitHub repository](https://github.com/Aerosol-Lab/TDMA_measurements).
[![TDMA-measurements](https://user-images.githubusercontent.com/62391931/229002061-9c3ec45d-a4f5-4414-8076-6cedfea41ca8.png)](https://github.com/Aerosol-Lab/TDMA_measurements)

* **DMA-Scan:** (Python) This code allows controlling a single DMA, and its corresponding high-voltage unit using a DAQ for scan measurements of nanoparticle size. This code includes GUI (see the picture below) to introduce parameters and run the experiments. This code was mainly developed by Dr. Tomoya Tamadate but I have also contributed to its development. It is available through the following [GitHub repository](https://github.com/Aerosol-Lab/DMAscan).
[![Screenshot from 2023-05-01 08-50-06](https://user-images.githubusercontent.com/62391931/235461216-2eca5ee1-7e2f-4a95-b711-918d4e5f2429.png)](https://github.com/Aerosol-Lab/TDMA_measurements)

[Teaching and tutorials](./teaching-tutorials.html)

[Return to Home](./index.html)
