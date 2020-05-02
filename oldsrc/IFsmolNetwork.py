import functools
import numpy as np
import math
from scipy.integrate import solve_ivp
import matplotlib
import matplotlib.pyplot as plt

#Possibly worth mentioning or reimplementing
from collections import deque

# Global Parameters
T_MAX = 100    # ms - Time to Run
DT = 0.1        # ms - Time Step
T_COUNT = int(T_MAX/DT)
T_ARR = np.linspace(0, T_MAX, T_COUNT)

TAU_S = 8  # Time constant of all synapses
S_DEL = 15  # Delay in signals

class LIF():
    def __init__(self, v_rest, v_max, R, C, I_ext, I_output, inputs=[]):
        self.v_rest = v_rest
        self.v_max = v_max
        self.tau = R*C
        self.R = R

        # Currents
        self.I_ext = I_ext
        self.I_output = I_output

        # Initial spike time and v_m values
        self.last_spikes = deque(maxlen=2)
        self.v_m = v_rest

        # Array of input LIFs
        self.inputs = inputs

         # spike and v recording arrays
        self.v_arr = np.zeros(T_COUNT)
        self.s_arr = np.zeros(T_COUNT, np.int8)

    def dv_dt(self, t_index, v):
        return (-v + self.v_rest + self.R*self.I(t_index))/self.tau

    # SIDE-EFFECTS
    def getv_m(self, t_index):
        if self.v_m >= self.v_max: 
            self.v_m = self.v_rest
            self.last_spikes.append(t_index)
            self.s_arr[t_index] = 1     # Can be optional: if recording
        self.v_m = self.v_m + DT*self.dv_dt(t_index, self.v_m)
        self.v_arr[t_index] = self.v_m  # Can be optional: if recording
        return self.v_m

    def getDecayedOutput(self, t_index):
        out = 0.0
        for s_tidx in self.last_spikes:
            t_decay = (t_index - s_tidx) * DT - S_DEL
            if t_decay < 0 or t_decay > 4*TAU_S: 
                continue
            else: 
                out += self.I_output * math.exp(-t_decay/TAU_S)
        return out

    def I(self, t_index):
        return functools.reduce(
            lambda acc, y: acc + y.getDecayedOutput(t_index),  # Sum all the decayed outputs
            self.inputs,    # Input list to reduce
            self.I_ext()      # Inital state of accumulator
        )

in_lif  =   LIF(0,  10, 6,  2,  lambda : 2,  4)
out_lif =   LIF(0,  10, 6,  2,  lambda : 0,1,[in_lif])

for i in range(T_COUNT):
    print(in_lif.getv_m(i))
    print(out_lif.getv_m(i))

print(in_lif.v_arr)
print(out_lif.v_arr)

fig, (ax1, ax2) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [1, 3]})

ax1.plot(T_ARR, in_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.plot(T_ARR, out_lif.s_arr, marker='.', markersize=20, linestyle='none')
ax1.set(ylabel='Spikes')
ax1.axis([0,T_MAX, 0.5, 1.5])
ax1.set_yticklabels([])
ax1.set_yticks([])

ax2.plot(T_ARR, in_lif.v_arr)
ax2.plot(T_ARR, out_lif.v_arr)
ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
ax2.grid()


fig.savefig("dualSpikingNeuron.png")
plt.show()
