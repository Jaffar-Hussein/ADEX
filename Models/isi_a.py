from brian2 import *
import matplotlib.pyplot as plt
import numpy
from pandas import DataFrame

a_val = list(range(1, 10))

eqs = eqs = """
    dvm/dt = (g_l*(e_l - vm) + g_l*d_t*exp((vm-v_t)/d_t) + i_stim - w)/c_m : volt (unless refractory)
    dw/dt  = (a*(vm - e_l) - w)/a_w : amp
    """

a_values = []
isi_values = []
for i in a_val:
    parameters = {
        "c_m": 200 * pF,
        "g_l": 10.*nS,
        "e_l": -65.*mV,
        "v_t": -55.*mV,
        "d_t": 5.0*mV,
        "a": i * nS,
        "a_w": 500.0*ms,
        "b": 10.0*pA,
        "v_r": -52*mV,
        "i_stim": .120*nA,
    }
    neuron = NeuronGroup(
        1,
        model=eqs,
        threshold="vm > -40.*mV",
        reset="vm = v_r; w += b",
        refractory='5*ms',
        method="euler",
        namespace=parameters,
    )
    neuron.vm = parameters["e_l"]
    neuron.w = 0
    states = StateMonitor(neuron, ["vm", "w"], record=True, when="thresholds")
    defaultclock.dt = 0.1 * ms
    train = SpikeMonitor(neuron, record=True)
    run(4000 * ms)

    vms = np.clip(states[0].vm / mV, a_min=None, a_max=0)
    
    difference = numpy.diff(train.spike_trains()[0])
    # print(difference)
    # break
    # difference = numpy.around(difference, 1)
    # difference = numpy.unique(difference)

    for j in difference:
        a_values.append(i)
        isi_values.append(j)

df = DataFrame({'variable': a_values, 'isi': isi_values})


def a_plt(df):
    plt.figure(figsize=(10,5),dpi=300, tight_layout=True)
    plt.title("Change in inter spike interval by a")
    plt.xlabel('Variation of a (nS)')
    plt.ylabel('Inter Spike Interval (s)')
    xlim(right=7.5)
    # plt.xlim(500,4000)
    plt.scatter(data=df, x='variable', y='isi', marker=",")
    plt.show()


if __name__ == '__main__':

    a_plt(df)
