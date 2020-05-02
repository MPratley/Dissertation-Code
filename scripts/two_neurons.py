import matplotlib.pyplot as plt

from neuron import LIF
from simulation import Simulation
from synapse import Synapse

# in_lif  =   LIF(0,  10, 6,  2,  lambda : 2,  4)
# out_lif =   LIF(0,  10, 6,  2,  lambda : 0,1,[in_lif])
sim = Simulation(200, 2000)
in_lif = LIF(sim, 0, 10, 6, 2, lambda: 2, [])
syn = Synapse(sim,in_lif,8,0,4)
out_lif = LIF(sim, 0, 10, 6, 2, lambda: 0, [syn])

for i in range(sim.t_itmax):
    print(in_lif.getv_m(i))
    print(out_lif.getv_m(i))

print(in_lif.v_arr)
print(out_lif.v_arr)

fig, (ax1, ax2) = plt.subplots(2, sharex=True,
                               gridspec_kw={'height_ratios': [1, 3]})

ax1.plot(sim.t_arr, in_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.plot(sim.t_arr, out_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.set(ylabel='Spikes')
ax1.axis([0, sim.t_max, 0.5, 1.5])
ax1.set_yticklabels([])
ax1.set_yticks([])

ax2.plot(sim.t_arr, in_lif.v_arr)
ax2.plot(sim.t_arr, out_lif.v_arr)
ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
ax2.grid()


fig.savefig("img/dualSpikingNeuron.png")
plt.show()

################################################################

sim = Simulation(200, 2000)
in_lif = LIF(sim, 0, 10, 6, 2, lambda: 2, [])
syn = Synapse(sim,in_lif,8,5,4)
out_lif = LIF(sim, 0, 10, 6, 2, lambda: 0, [syn])

for i in range(sim.t_itmax):
    print(in_lif.getv_m(i))
    print(out_lif.getv_m(i))

print(in_lif.v_arr)
print(out_lif.v_arr)

fig, (ax1, ax2) = plt.subplots(2, sharex=True,
                               gridspec_kw={'height_ratios': [1, 3]})

ax1.plot(sim.t_arr, in_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.plot(sim.t_arr, out_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.set(ylabel='Spikes')
ax1.axis([0, sim.t_max, 0.5, 1.5])
ax1.set_yticklabels([])
ax1.set_yticks([])

ax2.plot(sim.t_arr, in_lif.v_arr)
ax2.plot(sim.t_arr, out_lif.v_arr)
ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
ax2.grid()


fig.savefig("img/dualSpikingNeuronDelay.png")
plt.show()
