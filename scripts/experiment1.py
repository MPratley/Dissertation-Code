import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wasserstein_distance
from scipy.special import rel_entr
import pickle

from neuron import noise_wrapper
from simulation import Simulation
from neuron_group import NeuronGroup
from synapse_group import SynapseGroup
from synapse import Synapse
from util import plot_neuron_group, dist_arr
from typing import List

mean_absolute_dev_percs = [0,96]#[0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 96] # [0, 0.01, 0.025, 0.05]
root_two_over_pi = np.sqrt(np.divide(2, np.pi))**-1
sigs = [np.divide(np.divide(i, 100), root_two_over_pi)
        for i in mean_absolute_dev_percs]

output_neuron_varrs: List[List[float]] = []
timetotal = 2000
t_iter = 10000
tempsim = Simulation(timetotal, t_iter, stdp=False, name="unused")

for idx, sig in enumerate(sigs):
    SIM = Simulation(timetotal, t_iter, stdp=True, name="Sim{}".format(idx))
    np.random.seed(9943)

    FrequentNoisy = NeuronGroup(SIM, num_neurons=10, v_rest=noise_wrapper(0, 1, 0, 2), v_max=noise_wrapper(10, 1, 10, 8),
                                r=lambda: 6, c=lambda: 2, input_current_min=noise_wrapper(2, 1, 0, 3), starting_vm=noise_wrapper(5, 5, 0, 10))

    OccaisionalNoisy = NeuronGroup(SIM, num_neurons=10, v_rest=noise_wrapper(0, 1, 0, 2), v_max=noise_wrapper(10, 1, 10, 8),
                                   r=lambda: 6, c=noise_wrapper(5, 1, 3, 7), input_current_min=noise_wrapper(2, 3, -1, 3), starting_vm=noise_wrapper(5, 20, 0, 10))

    MidLayer = NeuronGroup(SIM, num_neurons=100, v_rest=lambda: 0, v_max=lambda: 10,
                           r=lambda: 6, c=lambda: 5, input_current_min=lambda: 0, starting_vm=noise_wrapper(7.5, 20, 0, 15))

    OutLayer = NeuronGroup(SIM, num_neurons=1, v_rest=lambda: 0, v_max=lambda: 1000,
                           r=lambda: 6, c=lambda: 5, input_current_min=lambda: 0, starting_vm=lambda: 0)

    weakSynapses = SynapseGroup(SIM, pre=FrequentNoisy, post=MidLayer, tau_s=lambda: 2, delay_MS=lambda: 5,
                                current_floor=lambda: 3, weight=noise_wrapper(0.5, 0.5, 0, 1), probTotal=500)

    StrongSynapses = SynapseGroup(SIM, pre=OccaisionalNoisy, post=MidLayer, tau_s=lambda: 8, delay_MS=lambda: 5,
                                  current_floor=lambda: 6, weight=noise_wrapper(0.5, 0.5, 0, 1), probTotal=400)

    for syn in SIM.synapses:
        syn.weight = max(syn.stdp_weight_min, min(
            syn.stdp_weight_max, np.random.normal(syn.weight, syn.weight*sig)))

    for neu in MidLayer.neurons:
        Synapse(SIM, neu, OutLayer.neurons[0], tau_s=1,
                delay_MS=0, current_floor=2, weight=1)

    SIM.run_simulation()
    print("")
    output_neuron_varrs.append(OutLayer.neurons[0].v_arr)

# pickle.dump(output_neuron_varrs, open("output_neuron_varrsSTDPON.p", "wb"))

# output_neuron_varrs = pickle.load( open( "output_neuron_varrsSTDPOFF.p", "rb" ) )

kul_arr: List[List[float]] = []
for idx, varr in enumerate(iterable=output_neuron_varrs, start=1):
    kul_arr.append(np.zeros(tempsim.t_itmax))
    rel_entr(output_neuron_varrs[0], varr,kul_arr[idx-1])

print(kul_arr)
pickle.dump(kul_arr, open("kulTimeSTDPONLONG.p", "wb"))


# dist_arr(output_neuron_varrs, tempsim.t_arr, "Time (ms)",
#          "Membrane Potential (mV)", [str(i) for i in mean_absolute_dev_percs])
# ems_arr = []

# for idx, varr in enumerate(iterable=output_neuron_varrs, start=1):
#     ems_arr.append(wasserstein_distance(output_neuron_varrs[0], varr))

# print(ems_arr)
# 

# plt.show()

# Results saved for easier processing
ems_arr_perm_nostdp = [0.0, 0.00016968780008990922, 0.00016968780008990922, 0.0006165431802204529, 0.0011329557644409974, 0.030561480773600193, 0.03117203470803437,
                       0.035787980651986406, 0.0773195642799105, 0.10622270129259588, 0.16360946107649546, 0.20672594860320143, 0.5350132418316609, 0.7718929718094749, 0.8402071828559441]
ems_arr_perm_stdp = [0.0, 0.0, 0.00018348201823509757, 0.00018348201823509757, 0.0007032264508136862, 0.0019013881737240583, 0.002947913462956008,
                     0.08381511320797105, 0.12252371728091674, 0.16652509931423648, 0.14379347004890292, 0.23419726457496232, 0.46374639215264113, 0.5292209390559082, 0.7382768079383011]


# fig, ax = plt.subplots()
# ax.plot(mean_absolute_dev_percs, ems_arr_perm_nostdp, label="STDP off")
# ax.plot(mean_absolute_dev_percs, ems_arr_perm_stdp, label="STDP on")
# ax.legend()
# plt.show()


#


# outSynapses = SynapseGroup(SIM, pre=MidLayer, post=OutLayer, tau_s=lambda: 1, delay_MS=lambda: 0,
#                    current_floor=noise_wrapper(2, 1, 0, 4), weight=lambda: 0, probTotal=200)


# SIM.run_simulation()
# plot_neuron_group(FrequentNoisy)
# plot_neuron_group(OccaisionalNoisy)
# plot_neuron_group(MidLayer)
# plot_neuron_group(OutLayer)
# plt.show()

# for perc in percentages:
#     pass


# NG2 = NeuronGroup(SIM, num_neurons=100, v_rest=lambda: 0, v_max=lambda: 10,
#                   r=lambda: 6, c=lambda: 3, input_current_min=lambda: 0)
# NG3 = NeuronGroup(SIM, num_neurons=10, v_rest=lambda: 0, v_max=lambda: 10,
#                   r=lambda: 6, c=lambda: 2, input_current_min=lambda: 0)
# # Be Careful using noise wrapper!
# # If you want certain things to be the same between runs,
# # remember to reset the seed
# SYG2 = SynapseGroup(SIM, pre=NG2, post=NG3, tau_s=lambda: 8, delay_MS=lambda: 2,
#                     current_floor=lambda: 4, weight=noise_wrapper(0.5, 0.5, 0, 1), probTotal=20)
