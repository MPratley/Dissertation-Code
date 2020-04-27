import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
import matplotlib.pyplot as plt

# Arbitrary Parameters
Tmax = 100  # ms - Time to Run
dt = 0.1    # ms - Time Step
Vrest = 0   # mV - Resting Voltage
Vmax = 10   # mV - Threshold Voltage
R = 6       # Ohms Resistance
C = 3       # mF - Capacitance
I = 2       # mA - Input Current
tau = R*C   # ms - Time Constant (7.5)

# Differential 
def dv_dt(t, v):
    return (-v + Vrest + R*I)/tau

t_arr = np.arange(0, Tmax, dt)
s_arr = np.zeros(len(t_arr))
v_arr = np.zeros(len(t_arr))
v_arr[-1] = Vrest

for i, t in enumerate(t_arr):
    Vm = v_arr[i-1]
    if Vm >= Vmax:
        Vm = Vrest
        s_arr[i] = 1
    else:
        Vm = Vm + dt*dv_dt(t, Vm)
    v_arr[i] = Vm

fig, (ax1, ax2) = plt.subplots(2, sharex=True)

ax1.plot(t_arr, s_arr, marker='.', markersize=20, linestyle='none')
ax1.set(ylabel='Spikes')
ax1.axis([0,Tmax, 0.5, 1.5])

ax2.plot(t_arr, v_arr)
ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
ax2.grid()


fig.savefig("singleSpikingNeuron.png")
plt.show()

