import numpy as np


class LIF(object):

    def __init__(self, record=False, startPotential_V=0, refractoryPeriod_mS=4, threshold_V=1):
        self.resistance = 1 # resistance (kOhm)
        self.capacitance = 10 # capacitance (uF)
        self.V_spike = 0.5 # spike delta (V)
        self.tau = self.resistance*self.capacitance # time constant (msec)

        self.potential = startPotential_V
        if record is True:
            self.potentialHistory = [self.potential]

        self.tau_ref = refractoryPeriod_mS
        self.Vth = threshold_V

    



## setup parameters and state variables
T = 50 # total time to simulate (msec)
dt = 0.125 # simulation time step (msec)
time = range(0, T+dt, dt) # time array
t_rest = 0 # initial refractory time

## Input stimulus
I = 1.5 # input current (A)
## iterate over each time step
for i, t in enumerate(time):
 if t > t_rest:
    Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
 if Vm[i] >= Vth:
    Vm[i] += V_spike
    t_rest = t + tau_ref
## plot membrane potential trace
# plot(time, Vm)
# title('Leaky Integrate-and-Fire Example')
# ylabel('Membrane Potential (V)')
# xlabel('Time (msec)')
# ylim([0,2])
# show()