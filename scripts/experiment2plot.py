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
timetotal = 2000
t_iter = 10000
tempsim = Simulation(timetotal, t_iter, stdp=False, name="unused")
mean_absolute_dev_percs = [0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 96]
xnew = np.linspace(min(mean_absolute_dev_percs), max(mean_absolute_dev_percs), 300) 

#Results saved for easier processing
KL_arr_perm_nostdp = output_neuron_varrs = pickle.load( open( "kulTimeSTDPOFFLONG.p", "rb" ) )
                     
KL_arr_perm_stdp = output_neuron_varrs = pickle.load( open( "kulTimeSTDPONLONG.p", "rb" ) )
                     


# z1 = np.polyfit(mean_absolute_dev_percs, ems_arr_perm_nostdp, 1)
# p1 = np.poly1d(z1)
# z2 = np.polyfit(mean_absolute_dev_percs, ems_arr_perm_stdp, 1)
# p2 = np.poly1d(z2)

fig, ax = plt.subplots()
ax.plot(tempsim.t_arr, KL_arr_perm_nostdp[-1],label="STDP off")
ax.plot(tempsim.t_arr, KL_arr_perm_stdp[-1], label="STDP on")
ax.set(xlabel="Time (ms)", ylabel="Relative Entropy (KL-Divergence)")
ax.legend()
plt.show()