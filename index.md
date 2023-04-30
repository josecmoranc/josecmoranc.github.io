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
* **Fractal-like agglomerate morphology and radiative properties (theoretical and numerical)**
* **Aerosol metrology (experimental)**
* **Others (numerical)**

## 2. Numerical tools

## 3. Teaching and Tutorials

## 4. Scientific presentations

## 5. Outreach
