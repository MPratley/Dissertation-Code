import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import wasserstein_distance, entropy
import matplotlib
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [1, 3]})
fig2, (ay1,ay2) = plt.subplots(1,2)


# Arbitrary Parameters
Tmax = 1000  # ms - Time to Run
dt = 0.001   # ms - Time Step
Vrest = 0   # mV - Resting Voltage
Vmax = 10   # mV - Threshold Voltage
R = 6       # Ohms Resistance
C = 3       # mF - Capacitance
I = 2       # mA - Input Current
tau = R*C   # ms - Time Constant (7.5)

# Differential 
def dv_dt(t, v):
    return (-v + Vrest + R*I)/tau

t_arr_b = np.arange(0, Tmax, dt)
s_arr_b = np.zeros(len(t_arr_b))
v_arr_b = np.zeros(len(t_arr_b))
v_arr_b[-1] = Vrest

#BASELINE
for i, t in enumerate(t_arr_b):
    Vm = v_arr_b[i-1]
    if Vm >= Vmax:
        Vm = Vrest
        s_arr_b[i] = 1
    else:
        Vm = Vm + dt*dv_dt(t, Vm)
    v_arr_b[i] = Vm

def vcomparr(dtval,v_arr):
    vcomp = []
    for idx, v in enumerate(v_arr):
        if (idx * dtval) % 2 == 0:
            vcomp.append(v)
    return vcomp

vcomp_b = vcomparr(dt, v_arr_b)
tcomp = vcomparr(dt, t_arr_b)

entropyarr = []
emsarr = []
dtnarr = [0.005, 0.01,0.025,0.05, 0.1,0.25,0.5,1,2]
# dtnarr = [0.01]

# ERRORLOOP
for dtn in dtnarr:
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
    
    vcomp_dtn = vcomparr(dtn,v_arr)

    label = "dt={}".format(dtn)
    # ay1.plot(tcomp, vcomp_dtn, label=label)
    emsarr.append(wasserstein_distance(vcomp_dtn, vcomp_b))
    entropyarr.append(entropy (vcomp_dtn, vcomp_b))

    ax2.plot(t_arr, v_arr, label=label)
    ax1.plot(t_arr, s_arr, marker='.', markersize=20, linestyle='none')

ay1.bar(["%.3f" % number for number in dtnarr],entropyarr, color='b')
ay1.set(xlabel='dt (ms)', ylabel='Relative Entropy to dt = 0.001')
ay1.grid()

ay2.bar(["%.3f" % number for number in dtnarr],emsarr, color='g')
ay2.set(xlabel='dt (ms)', ylabel='Wasserstein metric (EMD) from dt = 0.001 (mV)')
ay2.grid()

# ax1.set(ylabel='Spikes')
# ax1.axis([0,Tmax, 0.5, 1.5])
# ax1.set_yticklabels([])
# ax1.set_yticks([])

# ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
# ax2.grid()
# ax2.legend()

# fig.savefig("singleSpikingNeurondt.eps")

plt.show()