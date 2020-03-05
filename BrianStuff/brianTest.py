from brian2.units import ms
from brian2 import NeuronGroup, Synapses, StateMonitor, run
import matplotlib.pyplot as plt

eqs = '''
dv/dt = (I-v)/tau : 1
I : 1
tau : second
'''

G = NeuronGroup(3, eqs, threshold='v>1', reset='v = 0', method='exact')
G.I = [2, 2, 0]
G.tau = [10, 5, 100]*ms

# Comment these two lines out to see what happens without Synapses
S = Synapses(G, G, on_pre='v_post += 0.2')
S.connect(i=0, j=2)
S.connect(i=1, j=2)


M = StateMonitor(G, 'v', record=True)

run(100*ms)

plt.plot(M.t/ms, M.v[0], label='Neuron 0')
plt.plot(M.t/ms, M.v[1], label='Neuron 1')
plt.plot(M.t/ms, M.v[2], label='Neuron 2')
plt.xlabel('Time (ms)')
plt.ylabel('v')
plt.legend()
plt.show()