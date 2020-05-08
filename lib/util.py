import matplotlib.pyplot as plt
from neuron_group import NeuronGroup
from typing import List


def plot_neuron_group(ng: NeuronGroup):
    fig, (ax1, ax2) = plt.subplots(2, sharex=True,
                                   gridspec_kw={'height_ratios': [1, 3]})

    for neu in ng.neurons:
        ax1.plot(neu.simulation.t_arr, neu.s_arr, marker='.',
                 markersize=20, linestyle='none')
        # ax1.plot(neu.simulation.t_arr, neu.inputs[0].pre.s_arr,
        #          marker='.', markersize=20, linestyle='none')
        ax1.set(ylabel='Spikes')
        ax1.axis([0, neu.simulation.t_max, 0.5, 1.5])
        ax1.set_yticklabels([])
        ax1.set_yticks([])

        ax2.plot(neu.simulation.t_arr, neu.v_arr)
        # ax2.plot(neu.simulation.t_arr, neu.inputs[0].pre.v_arr)
        ax2.set(xlabel='time (ms)', ylabel='voltage (mV)')
        ax2.grid()
    return fig, [ax1, ax2]


def dist_arr(arrs: List[List[float]], x_axis, xlabel, ylabel, labelArr = None):
    # fig, (ax1, ax2) = plt.subplots(2, sharex=True,
    #                                gridspec_kw={'height_ratios': [1, 3]})
    fig, ax2 = plt.subplots()

    for idx, arr in enumerate(arrs):
        # ax1.plot(neu.simulation.t_arr, neu.s_arr, marker='.',
        #          markersize=20, linestyle='none')
        # # ax1.plot(neu.simulation.t_arr, neu.inputs[0].pre.s_arr,
        # #          marker='.', markersize=20, linestyle='none')
        # ax1.set(ylabel='Spikes')
        # ax1.axis([0, neu.simulation.t_max, 0.5, 1.5])
        # ax1.set_yticklabels([])
        # ax1.set_yticks([])

        ax2.plot(x_axis, arr, label="idx={}".format(idx))
        if labelArr:
            ax2.legend(labelArr)
        else:
            ax2.legend()
        # ax2.plot(neu.simulation.t_arr, neu.inputs[0].pre.v_arr)
        ax2.set(xlabel=xlabel, ylabel=ylabel)
        ax2.grid()
    return fig, ax2
