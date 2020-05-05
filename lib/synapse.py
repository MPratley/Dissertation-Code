import math

import simulation
import neuron


class Synapse():
    def __init__(self, sim: simulation.Simulation, pre: 'neuron.LIF', post: 'neuron.LIF',
                 tau_s: float, delay_MS: float, current_floor: float, weight: float = 1):
        self.simulation = sim.register_synapse(self)
        self.pre = pre
        self.post = post
        post.inputs.append(self)
        self.weight = weight
        self.tau_s = tau_s
        self.delay = delay_MS
        self.current_floor = current_floor

        self.stdp_weight_max = 1
        self.stdp_weight_min = 0.1
        self.stdp_a_minus = 0.3
        self.stdp_a_plus = 0.6
        self.stdp_tau_plus = 8
        self.stdp_tau_minus = 2 #5
        self.stdp_ltp_time = 2
        self.stdp_ltd_time = -1

    def get_decayed_output(self, t_index):
        """
        Given the last `len(last_spikes)` spikes, what's the output current from the neuron.

        Arguments:
            t_index {int} -- The relative time-index of the output

        Returns:
            float -- The ouput current
        """
        if t_index != self.pre.t_curr_idx:
            # tick pre if it's not at the right tickidx
            self.pre.getv_m(t_index)
        out = 0.0
        for s_tidx in self.pre.last_spikes:
            t_decay = (t_index - s_tidx) * self.simulation.d_t - self.delay
            if t_decay < 0 or t_decay > 4*self.tau_s:
                continue
            out += self.current_floor * math.exp(-t_decay/self.tau_s)
        return out*self.weight

    def weight_adjust(self):
        w_delta = 0
        for tf_post_idx in self.post.last_spikes:
            for tf_pre_idx in self.pre.last_spikes:
                delta_t = (tf_post_idx-tf_pre_idx) * \
                    self.simulation.d_t - self.delay
                stdp = self.stdp(delta_t)
                if stdp > 0:
                    # Times learning rate if I choose to have one
                    w_delta += self.simulation.d_t * stdp * (self.stdp_weight_max - self.weight)
                else:
                    # Same as above
                    w_delta += self.simulation.d_t * stdp * (self.weight - self.stdp_weight_min)
        self.weight = max(self.stdp_weight_min, min(
            self.stdp_weight_max, self.weight+w_delta)) # Clamp the weight

    def stdp(self, delta_t):
        if delta_t <= self.stdp_ltd_time:
            return self.stdp_a_minus * math.exp(delta_t/self.stdp_tau_minus)
        if delta_t >= self.stdp_ltp_time:
            return self.stdp_a_plus * math.exp(delta_t/self.stdp_tau_plus)
        return 0
