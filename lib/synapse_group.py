from typing import Callable, List
import numpy as np

import simulation
import neuron
import synapse
import neuron_group


class SynapseGroup():
    def __init__(self, sim: simulation.Simulation, pre: neuron_group.NeuronGroup, post: neuron_group.NeuronGroup,
                 tau_s: Callable[[], float], delay_MS: Callable[[], float], current_floor: Callable[[], float], weight: Callable[[], float],
                 probTotal: int = None, probConnection: float = None):
        if probTotal and probConnection:
            raise ValueError("Can't set both probTotal and probConnection")
        if probTotal:
            size = len(pre.neurons)*len(post.neurons)
            probConnection = probTotal / size

        self.synapses: List[synapse.Synapse] = []

        for pre_n in pre.neurons:
            for post_n in post.neurons:
                if np.random.uniform() < probConnection:
                    syn = synapse.Synapse(
                        sim, pre_n, post_n, tau_s(), delay_MS(), current_floor(), weight())
                    self.synapses.append(syn)
    