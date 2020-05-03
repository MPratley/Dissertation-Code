import numpy as np
import neuron
import synapse


class Simulation():
    def __init__(self, time_simulated_ms: float, time_iterations: int):
        # Time stuff
        self.t_max = time_simulated_ms
        self.t_itmax = time_iterations
        self.d_t = time_simulated_ms/time_iterations
        self.t_arr = np.linspace(0, self.t_max, self.t_itmax)

        # Neurons in this simulation
        self.neurons: 'neuron.LIF' = []
        self.synapses: 'synapse.Synapse' = []

    def register_neuron(self, neu: 'neuron.LIF'):
        self.neurons.append(neu)
        return self

    def register_synapse(self, syn: 'synapse.Synapse'):
        self.synapses.append(syn)
        return self

    def run_simulation(self):
        for i in range(self.t_itmax):
            for neu in self.neurons:
                neu.getv_m(i)
            for syn in self.synapses:
                syn.weight_adjust()
            perc = (100*i)//self.t_itmax
            if perc % 5 == 0:
                print("\t{} percent complete".format(perc), end='\r')
