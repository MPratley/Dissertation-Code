import matplotlib.pyplot as plt

from neuron import noise_wrapper
from simulation import Simulation
from neuron_group import NeuronGroup
from synapse_group import SynapseGroup

fig, (ax1, ax2) = plt.subplots(2, sharex=True,
                               gridspec_kw={'height_ratios': [1, 3]})

SIM = Simulation(100, 1000)
NG1 = NeuronGroup(SIM, num_neurons=100, v_rest=noise_wrapper(0, 1, 0, 2), v_max=noise_wrapper(10, 1, 10, 8),
                  r=lambda: 6, c=lambda: 2, input_current_min=noise_wrapper(2, 2), starting_vm=noise_wrapper(5, 5, 0, 10))
NG2 = NeuronGroup(SIM, num_neurons=100, v_rest=lambda: 0, v_max=lambda: 10,
                  r=lambda: 6, c=lambda: 2, input_current_min=lambda: 0)
# Be Careful using noise wrapper!
# If you want certain things to be the same between runs,
# remember to reset the seed
SYG = SynapseGroup(SIM, pre=NG1, post=NG2, tau_s=lambda: 8, delay_MS=lambda: 5,
                   current_floor=lambda: 5, weight=noise_wrapper(1, 0.25), probTotal=200)

SIM.run_simulation()

# print(len(SYG.synapses))

for idx, n in enumerate(NG2.neurons):
    if len(n.inputs) > 0:
        print(n.v_arr)
        ax1.plot(SIM.t_arr, n.s_arr, marker='.',
                 markersize=20, linestyle='none')
        ax1.plot(SIM.t_arr, n.inputs[0].pre.s_arr, marker='.', markersize=20, linestyle='none')
        ax1.set(ylabel='Spikes')
        ax1.axis([0, SIM.t_max, 0.5, 1.5])
        ax1.set_yticklabels([])
        ax1.set_yticks([])

        ax2.plot(SIM.t_arr, n.v_arr)
        ax2.plot(SIM.t_arr, n.inputs[0].pre.v_arr)
        ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
        ax2.grid()
        break
    # print(idx)
    # print(n.t_curr_idx)
        # print(n.input_current(99))
        # print(n.getv_m(100))

plt.show()
