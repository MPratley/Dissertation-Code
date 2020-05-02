import functools
from collections import deque  # Possibly worth mentioning or reimplementing
from typing import List, MutableSequence, Callable

import numpy as np
import synapse
import simulation


def noisy_input(mean_current: float, sigma_noise: float):
    return np.random.normal(mean_current, sigma_noise)

class LIF():
    def __init__(self, sim: simulation.Simulation, v_rest: float, v_max: float, r: float, c: float,
                 input_current_min: Callable[[], float], input_synapses: List['synapse.Synapse']):
        self.simulation = sim
        self.v_rest = v_rest
        self.v_max = v_max
        self.tau = r*c
        self.resistance = r

        # Currents
        self.input_current_min = input_current_min

        # Initial spike time and v_m values
        self.last_spikes: MutableSequence = deque(maxlen=2)
        self.v_m = v_rest

        # Array of input LIFs
        self.inputs = input_synapses

        # spike and v recording arrays
        self.v_arr = np.zeros(self.simulation.t_itmax)
        self.s_arr = np.zeros(self.simulation.t_itmax, np.int8)
        self.t_curr_idx = 0

    def input_current(self, t_index):
        return functools.reduce(
            # Sum all the decayed outputs
            lambda acc, y: acc + y.get_decayed_output(t_index),
            self.inputs,    # Input list to reduce
            self.input_current_min()      # Inital state of accumulator
        )

    def dv_dt(self, t_index, potential):
        return (-potential + self.v_rest + self.resistance*self.input_current(t_index))/self.tau

    # SIDE-EFFECTS - this is not a thread safe implementation
    def getv_m(self, t_index):
        if self.t_curr_idx == t_index:
            return self.v_m
        if self.t_curr_idx + 1 == t_index:
            self.t_curr_idx += 1
            if self.v_m >= self.v_max:
                self.v_m = self.v_rest
                self.last_spikes.append(t_index)
                self.s_arr[t_index] = 1     # Can be optional: if recording
            self.v_m = self.v_m + self.simulation.d_t * \
                self.dv_dt(t_index, self.v_m)
            self.v_arr[t_index] = self.v_m  # Can be optional: if recording
            return self.v_m
        raise ValueError("too large a jump: {}!".format(t_index-self.t_curr_idx))
