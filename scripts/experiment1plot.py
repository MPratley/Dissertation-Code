import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wasserstein_distance
import pickle
from scipy.interpolate import make_interp_spline, BSpline


from neuron import noise_wrapper
from simulation import Simulation
from neuron_group import NeuronGroup
from synapse_group import SynapseGroup
from synapse import Synapse
from util import plot_neuron_group, dist_arr
from typing import List

plt.style.use('seaborn-whitegrid')

mean_absolute_dev_percs = [0, 0.01, 0.025, 0.05,
                           0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 96]
xnew = np.linspace(min(mean_absolute_dev_percs), max(mean_absolute_dev_percs), 300) 

#Results saved for easier processing
ems_arr_perm_nostdp = [0.0, 0.00016968780008990922, 0.00016968780008990922, 0.0006165431802204529, 0.0011329557644409974, 0.030561480773600193, 0.03117203470803437,
                       0.035787980651986406, 0.0773195642799105, 0.10622270129259588, 0.16360946107649546, 0.20672594860320143, 0.5350132418316609, 0.7718929718094749, 0.9402071828559441]
ems_arr_perm_stdp = [0.0, 0.0, 0.00018348201823509757, 0.00018348201823509757, 0.0007032264508136862, 0.0019013881737240583, 0.002947913462956008,
                     0.08381511320797105, 0.12252371728091674, 0.16652509931423648, 0.14379347004890292, 0.23419726457496232, 0.46374639215264113, 0.5292209390559082, 0.6982768079383011]


z1 = np.polyfit(mean_absolute_dev_percs, ems_arr_perm_nostdp, 1)
p1 = np.poly1d(z1)
z2 = np.polyfit(mean_absolute_dev_percs, ems_arr_perm_stdp, 1)
p2 = np.poly1d(z2)

fig, ax = plt.subplots()
plt.xscale("log")
ax.plot(mean_absolute_dev_percs, ems_arr_perm_nostdp,label="STDP off")
ax.plot(mean_absolute_dev_percs, ems_arr_perm_stdp, label="STDP on")
ax.set(xlabel="Mean Synaptic Weight Error (%)", ylabel="Earth Movers' Distance (mV)")
ax.legend()
plt.show()