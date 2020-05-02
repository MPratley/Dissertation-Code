import math

import simulation
import neuron

class Synapse():
    def __init__(self, sim: simulation.Simulation, pre: 'neuron.LIF',
                 tau_s: float, delay_MS: float, current_floor: float, weight: float = 1):
        self.simulation = sim
        self.pre = pre
        self.weight = weight
        self.tau_s = tau_s
        self.delay = delay_MS
        self.current_floor = current_floor

    def get_decayed_output(self, t_index):
        """Given the last `len(last_spikes)` spikes, what's the output current from the neuron.

        Arguments:
            t_index {int} -- The relative time-index of the output

        Returns:
            float -- The ouput current
        """
        out = 0.0
        for s_tidx in self.pre.last_spikes:
            t_decay = (t_index - s_tidx) * self.simulation.d_t - self.delay
            if t_decay < 0 or t_decay > 4*self.tau_s:
                continue
            out += self.current_floor * math.exp(-t_decay/self.tau_s)
        return out
