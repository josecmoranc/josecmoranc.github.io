import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import configparser
from scipy.special import gamma
from scipy.optimize import fsolve

# New version of physical model
def import_physical_model(path):
    cols = ["time","Nagg","fv","np_avg","T","box_volume","Npp","u_sr","J_nuc"]
    # particles number concentration, n (#/cm^3)
    physical_model0 = pd.read_csv(path, sep="\s+",\
                      names=cols, dtype='float')
    physical_model0.set_index(["time"], inplace = True)
    return physical_model0

