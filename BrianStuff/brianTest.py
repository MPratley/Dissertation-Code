from brian2.units import ms
from brian2 import NeuronGroup, Synapses, StateMonitor, run
import matplotlib.pyplot as plt
import numpy as np

eqs = '''
dv/dt = (I-v)/tau : 1
I : 1
tau : second
'''

# Predefined seed so the experiment is repeatable.
np.random.seed(67726)

DrivingGroup = NeuronGroup(9, eqs, threshold='v>1', reset='v = 0', method='exact')
DrivingGroup.I = np.random.uniform(low=0, high=2, size=9)
DrivingGroup.tau = np.full(
    shape=9,
    fill_value=10,
    dtype=np.int)*ms

# DrivingGroup.tau = [10, 5, 100]*ms

OutputGroup = NeuronGroup(1, eqs, threshold='v>2', reset='v = 0', method='exact')
OutputGroup.I = [0]
OutputGroup.tau = [100]*ms

# Comment these two lines out to see what happens without Synapses
S = Synapses(DrivingGroup, OutputGroup, on_pre='v_post += 0.2')
S.connect(i=np.arange(9), j=0)
# S.connect(i=0, j=2)
# S.connect(i=1, j=2)

DrivingMonitor = StateMonitor(DrivingGroup, 'v', record=True)
OutputMonitor = StateMonitor(OutputGroup, 'v', record=True)

def visualise_connectivity(S):
    Ns = len(S.source)
    Nt = len(S.target)
    plt.figure(figsize=(3, 6))
    # plt.subplot(121)
    plt.plot(np.zeros(Ns), np.arange(Ns), 'ok', ms=10)
    plt.plot(np.ones(Nt), np.arange(Nt), 'ok', ms=10)
    for i, j in zip(S.i, S.j):
        plt.plot([0, 1], [i, j], '-k')
    # plt.xticks([0, 1], ['Source', 'Target'])
    # plt.ylabel('Neuron no.')
    plt.xlim(-0.1, 1.1)
    plt.ylim(-1, max(Ns, Nt))
    # plt.subplot(122)
    # plt.plot(S.i, S.j, 'ok')
    # plt.xlim(-1, Ns)
    # plt.ylim(-1, Nt)
    # plt.xlabel('Source neuron index')
    # plt.ylabel('Target neuron index')

visualise_connectivity(S)
plt.axis('off')
plt.savefig('2.png', transparent=True)


# run(100*ms)

# plt.figure()
# plt.plot(DrivingMonitor.t/ms, DrivingMonitor.v[0], label='Input Neuron 1 of 9')
# plt.plot(OutputMonitor.t/ms, OutputMonitor.v[0], label='Output Neuron')
# # plt.plot(M.t/ms, M.v[1], label='Neuron 1')
# # plt.plot(M.t/ms, M.v[2], label='Neuron 2')
# plt.xlabel('Time (ms)')
# plt.ylabel('v')
# plt.legend()
# plt.show()
# plt.savefig('1.png')