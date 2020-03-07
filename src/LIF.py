import numpy as np
from typing import List
from Synapse import Synapse


class LIF(object):

    def __init__(self, record:bool = False, startPotential_V:float=0, threshold_V:float=1, refractoryPeriod_mS:int=4):
        self.simulatedTime:float = 0
        self.resistance = 1  # resistance (kOhm)
        self.capacitance = 10  # capacitance (uF)
        self.V_spike = 0.5  # spike delta (V)
        self.tau = self.resistance*self.capacitance  # time constant (msec)

        # Double Linking of nodes
        self.inputSynapses:List[Synapse] = []
        self.outputSynapses:List[Synapse] = []

        self.potential = startPotential_V
        if record is True:
            self.potentialHistory = [self.potential]

        self.tau_ref = refractoryPeriod_mS
        self.Vth = threshold_V

    def potentialAt(self, simulatedTime:float):
        print("Unfinished")

    # def step(self, deltaTmS:float):
    #     print("yeet")
        # Something like this boi
        # for i, t in enumerate(time):
        #     if t > t_rest:
        #         Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
        #     if Vm[i] >= Vth:
        #         Vm[i] += V_spike
        #         t_rest = t + tau_ref



# # setup parameters and state variables
# T = 50  # total time to simulate (msec)
# dt = 0.125  # simulation time step (msec)
# time = range(0, T+dt, dt)  # time array
# t_rest = 0  # initial refractory time

# # Input stimulus
# I = 1.5  # input current (A)
# # iterate over each time step
# for i, t in enumerate(time):
#     if t > t_rest:
#         Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
#     if Vm[i] >= Vth:
#         Vm[i] += V_spike
#         t_rest = t + tau_ref
# plot membrane potential trace
# plot(time, Vm)
# title('Leaky Integrate-and-Fire Example')
# ylabel('Membrane Potential (V)')
# xlabel('Time (msec)')
# ylim([0,2])
# show()
