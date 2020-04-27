import numpy as np 
from scipy.integrate import solve_ivp


# Parameters
Tmax = 100  # ms - Time to Run
dt = 0.1    # ms - Time Step
numSteps = int(Tmax/dt)
Vmax = 50   # mV - Threshold Voltage
R = 5       # Ohms Resistance
C = 2       # mF - Capacitance
I = 1.5     # mA - Input Current
tau = R*C   # ms - Time Constant (7.5)

def dv_dt(t, v):
    if v >= Vmax:
        return -Vmax
    return (-v + R*I)/tau

t_arr = np.linspace(0,Tmax,numSteps)
v0 = [0]
sol = solve_ivp(dv_dt, [0,Tmax], v0, t_eval=t_arr)




