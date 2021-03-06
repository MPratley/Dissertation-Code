import math
from typing import Callable

import simulation
import neuron
import synapse


class NeuronGroup():
    def __init__(self, sim: simulation.Simulation, num_neurons: int, v_rest: Callable[[], float],
                 v_max: Callable[[], float], r: Callable[[], float], c: Callable[[], float],
                 input_current_min: Callable[[], float],  starting_vm: Callable[[], float] = None):
        self.neurons = [
            neuron.LIF(sim, v_rest(), v_max(), r(), c(), input_current_min, [], starting_vm() if starting_vm else v_rest())
            for i in range(num_neurons)
        ]

    
