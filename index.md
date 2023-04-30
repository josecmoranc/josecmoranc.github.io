---
layout: default
---

# Particle technology

## 1. About me and my research contributions

Since April 2022 I have been Post-doc Associate at [Hogan's Laboratory](https://hoganlab.umn.edu/) belonging to the Particle Technology Laboratory ([PTL](https://ptl.umn.edu/)) of the University of Minnesota. My domain of research is aerosol science with particular emphasis on multi-scale numerical simulations and experiments involving mainly nanoparticles. During my career I have investigated the following subjects:

* **Aerosol particle coagulation (theoretical & numerical)**
  - I derived an equation for the coagulation kernel of suspended particles valid in the transition of particle-particle interaction regime from a theoretical approach based on the Langevin equation. The new method reveals a likely universal asymptotic limit (long times) for the kinetics of coagulation. See [this paper](https://doi.org/10.3390/fractalfract6090529) or see [this presentation](https://doi.org/10.13140/RG.2.2.28226.66248) for further details.
![Screenshot from 2023-04-30 00-16-43](https://user-images.githubusercontent.com/62391931/235336902-4e379256-54fc-4931-b6e9-010d7fea1845.png)
  - I have introduced a unified self-preserving size distribution to describe particles formed during coagulation. I found the simultaneous transition in flow (from free molecular to continuum) and agglomeration regime (from ballistic to diffusive) to explain a systematic change in agglomerates morphology when increasing the size of primary particles (this was only experimentally observed before). See [this paper](https://doi.org/10.1016/j.jcis.2020.04.085) for further details.
 ![Screenshot from 2023-04-30 00-22-04](https://user-images.githubusercontent.com/62391931/235337088-66edb6ae-710d-426f-93f3-3df37993ed35.png)

* **New tools to simulate agglomerates and agglomeration (numerical)**
   - **FracVAL:** It is a tunable code to generate fractal-like agglomerates with prescribed fractal dimension, fractal prefactor, number of primary particles, and primary particle polydispersity. It is the only code able to take the polydispersity of primary particles into account in a rigorous way for a wide range of fractal parameters. It has been highly appreciated by different research groups around the world and the code has been used for particle-light interaction, particle hydrodynamics, morphology, and particle technology applications. The new version of this code including raspberry-like agglomerates and a self-avoiding random walk model for protein morphology. It will also include a module for numerical TEM image generation as I explain in [this presentation](https://gitlab.com/jmoranc1/fracval_cpp/-/blob/master/documents/JMoran_FracVAL_2021.pdf) and will be available through this [GitLab repository](https://gitlab.com/jmoranc1/fracval_cpp). In the same article, coworkers and I have introduced a volume-based pair correlation function to describe the morphology of agglomerates of nanoparticles. This method was adapted to more complex aggregates during my PhD thesis. This method has also been used by researchers interested in the morphology of liquid atomization particles (see the citations of [FracVAL paper](https://doi.org/10.1016/j.cpc.2019.01.015)).
![Screenshot from 2023-04-30 00-33-31](https://user-images.githubusercontent.com/62391931/235337377-ad89d38c-57f2-4cd7-8382-0fbe6ae179de.png)

   - **MCAC:** The Monte Carlo Aggregation Code is a discrete element modeling (DEM) approach to simulate nanoparticle coagulation. I discovered an optimized way to solve the Langevin equation, which is analogous to the DSMC used to solve the Boltzmann equation used in fluid mechanics, and validated the method theoretically based on a description of particle dynamics as random walks derived from a binomial statistical approach. See [this paper](https://doi.org/10.1016/j.jcis.2020.02.039) for further details. This code is avaialable through [CORIA-CFD GitHub](https://gitlab.coria-cfd.fr/MCAC/MCAC).
![Screenshot from 2023-04-30 00-42-53](https://user-images.githubusercontent.com/62391931/235337656-83690d7d-fabf-458f-a73c-2eb84ee97dea.png)

* **Simulating flame-made particle formation (numerical)**
  - I have explained the overlapping of primary particles formed in flames. Indeed, a long-standing question for soot formation in flames is if the overlapping of primary particles is linked to sintering or surface growth. I proposed the latter as the explanation as observed based on this MCAC simulations. In this work I was also able to simulate realistic soot particles that highly resemble those observed in experimental TEM images and was able to obtain a detailed morphological characterization of the simulated aggregates under 2 different flame conditions. See [this paper](https://doi.org/10.1016/j.jaerosci.2020.105690) for further details. 
![JAS-surface growth](https://ars.els-cdn.com/content/image/1-s2.0-S0021850220301750-fx1_lrg.jpg)

* **Characterization of flame-made particles (experimental)**
  - One fundamental question regarding flame-made particles formation is related to the unitary sticking probability of particles upon collisions which has been questioned in the literature. I have introduced a potential energy criterion to explain the transition from reaction-limited (sticking probability <<1) to diffusion-limited (sticking probability =1) nanoparticle coagulation regime at high temperatures. Particularly, I focused on a new approach to determine the rebound probability for fractal-like agglomerate collisions. This is the only work in the literature taking the van der Waals and electrostatic interactions into account in DEM simulations of nanoparticles formation under flame conditions. This is also the only work considering the evolution of soot maturity (here mainly manifested through a change in chemical composition and bulk density) into the coagulation kinetics.
![Carbon-sticking](https://ars.els-cdn.com/content/image/1-s2.0-S0008622321006722-ga1_lrg.jpg)

  - I have conducted line-of-sight attenuation (LOSA) measurements of soot volume fraction to decide on the particle sampling points in the flame. Once coworkers and I decided on those points, I conducted the thermophoretic sampling experiments and analyzed the data for comparison with the light-induced incandescence (LII) technique (mainly carried out by coworkers). I considerably improved the accuracy of the thermophoretic sampling technique based on LOSA technique to monitor the sampling in-situ. This is explained in detail in [this presentation](https://doi.org/10.13140/RG.2.2.10340.94087). See [this paper](https://doi.org/10.1016/j.fuel.2020.117030) for further details.
![Screenshot from 2023-04-30 01-04-47](https://user-images.githubusercontent.com/62391931/235338451-495f1390-fa0f-4c84-9880-37d929d33a8b.png)

  - I have analyzed a large database of flame-made particle transmission electron icroscopy (TEM) images to obtain morphological parameters of soot particles including their gyration diameter, number of monomers, projected area, among others. Here we studied three different fuels namely ethylene, propane and butane under different oxygen index conditions. See [this paper](https://pubs.acs.org/doi/10.1021/acs.energyfuels.8b01301) for further details.
 ![Screenshot from 2023-04-30 01-21-10](https://user-images.githubusercontent.com/62391931/235338940-d9f67d55-d4d0-40e2-842d-65c4d198fee3.png)
 
  - Coworkers and I have introduced a horizontal plana multi-angle light-scattering (HPALS) approach for measuring flame-made particle properties in-situ in the flame. We used a horizontal plane to avoid any volume-of-measurement bias in the data. I conducted the experimental measurements jointly with the first author and also developed the codes and post-processed the raw data including the deconvolution of measurements to obtain radially-resolved data. In this work we have conducted a highly spatially-resolved description of particle properties including their gyration diameter (the main property measured) as a function of the height above the buerner and at different radial positions. See [this paper](https://doi.org/10.1016/j.combustflame.2021.111539) for further details.
![Screenshot from 2023-04-30 01-18-13](https://user-images.githubusercontent.com/62391931/235338868-fc47ec94-3cc9-474f-b691-2f1f94bfc07e.png)
  - Coworkers and I have measured in-situ the evolution of soot particle maturity (characterized by the power-law exponent of the E(m) as a function of the wavelength) by combining LOSA and emission measurements at four different wavelengths (500, 532, 660 and 810 nm). Thanks to the accurate measurements conducted at the EC2G group (mainly by coworkers) we were able to reveal a map of soot maturity in the flame. In this paper, we made an effort to review different methods for soot maturity characterization as shown in the figure below. See [this paper](https://doi.org/10.1016/j.combustflame.2020.12.049) for further details.
 ![Screenshot from 2023-04-30 01-30-46](https://user-images.githubusercontent.com/62391931/235339216-8562a1eb-3734-4a50-a90b-029c8ff74990.png)

* **Fractal-like agglomerate morphology and radiative properties (theoretical and numerical)**
  - I have contributed to the development of a generalized model for agglomerates of nanoparticles morphology that explains the transition of the structure factor from a single primary particle to one of a fractal-like agglomerate. Jointly with the first author, we developed the equations of this work, where I particularly contributed to characterizing the pair correlation function of primary particles and I conducted the numerical simulations for comparison and using the simulations of this work. This article was selected as cover in the Journal of Aerosol Science.
![Screenshot from 2023-04-30 01-38-47](https://user-images.githubusercontent.com/62391931/235339488-ccad9bfc-59d7-4d6b-ab12-7b1ab85d2b60.png)

  - We investigated the role played by primary particle overlapping on the radiative properties of fractal-like agglomerates of nanoparticles. We thus obtained corrective factor to incorporate into the Rayleigh-Debye-Gans for fractal aggregates (RDG-FA). In addition, we observed an accurate and direct power-law between the radiative force and the aggregates volumetric volume. See [this paper](https://doi.org/10.1016/j.proci.2018.07.065) for further details.
![Screenshot from 2023-04-30 01-43-01](https://user-images.githubusercontent.com/62391931/235339598-404f8048-1a1d-419b-8e13-22eb61b9c7cc.png)

  - I have investigated the effect of primary particle polydispersity on the morphological properties of fractal-like aggregates derived from numericel TEM images. I showed analytically this effect based on Gaussian and Lognormal primary particle size distributions. I explored the Hough Transform algorithm for primary particle detection in numerical TEM images. See [this paper](https://doi.org/10.1016/j.powtec.2018.02.008) for further details.
![Screenshot from 2023-04-30 01-51-13](https://user-images.githubusercontent.com/62391931/235339904-71b43e4f-217a-4ef4-9e68-61e3fb0c9eec.png)

* **Aerosol metrology (experimental)**
* **Others (numerical)**

## 2. Numerical tools

## 3. Teaching and Tutorials

## 4. Scientific presentations

## 5. Outreach
