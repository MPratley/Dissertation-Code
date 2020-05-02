import numpy as np


class Simulation():
    def __init__(self, time_simulated_ms, time_iterations):
        # Time stuff
        self.t_max = time_simulated_ms
        self.t_itmax = time_iterations
        self.d_t = time_simulated_ms/time_iterations
        self.t_arr = np.linspace(0, self.t_max, self.t_itmax)

        # Neurons in this simulation
        self.neuron_individuals = []
        self.neuron_groups = []

    def register_neuron(self, neuron):
        print("temp")

    def register_neuron_group(self, neuron_group):
        print(self.t_max)

    def run_simulation(self):
        print(self.t_max)
