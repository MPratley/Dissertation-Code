import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [1, 3]})

# Arbitrary Parameters
Tmax = 150  # ms - Time to Run
# dt = 0.1    # ms - Time Step
Vrest = 0   # mV - Resting Voltage
Vmax = 10   # mV - Threshold Voltage
R = 6       # Ohms Resistance
C = 3       # mF - Capacitance
I = 2       # mA - Input Current
tau = R*C   # ms - Time Constant (7.5)

# Differential 
def dv_dt(t, v):
    return (-v + Vrest + R*I)/tau

for dtn in [0.01, 0.05, 0.1,0.2,0.5,1,2,4]:
    t_arr = np.arange(0, Tmax, dtn)
    s_arr = np.zeros(len(t_arr))
    v_arr = np.zeros(len(t_arr))
    v_arr[-1] = Vrest

    for i, t in enumerate(t_arr):
        Vm = v_arr[i-1]
        if Vm >= Vmax:
            Vm = Vrest
            s_arr[i] = 1
        else:
            Vm = Vm + dtn*dv_dt(t, Vm)
        v_arr[i] = Vm

    label = "dt={}".format(dtn)
    ax2.plot(t_arr, v_arr, label=label)
    ax1.plot(t_arr, s_arr, marker='.', markersize=20, linestyle='none')



ax1.set(ylabel='Spikes')
ax1.axis([0,Tmax, 0.5, 1.5])
ax1.set_yticklabels([])
ax1.set_yticks([])

ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
ax2.grid()

fig.savefig("singleSpikingNeurondt.png")
plt.show()

