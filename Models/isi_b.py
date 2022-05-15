from brian2 import *
import matplotlib.pyplot as plt
import numpy
from pandas import DataFrame

i_stim_val = [0.05, 0.06, 0.07, 0.08, 0.09,
              0.10, 0.15, 0.125, 0.175, 0.2, 0.25, 0.225]

eqs = eqs = """
    dvm/dt = (g_l*(e_l - vm) + g_l*d_t*exp((vm-v_t)/d_t) + i_stim - w)/c_m : volt (unless refractory)
    dw/dt  = (a*(vm - e_l) - w)/tau_w : amp
    """

stm_values = []
isi_values = []
for i in i_stim_val:
    parameters = {
        "c_m": 200 * pF,
        "g_l": 10.*nS,
        "e_l": -65.*mV,
        "v_t": -55.*mV,
        "d_t": 5.0*mV,
        "a": 2.0 * nS,
        "tau_w": 500.0*ms,
        "b": 10.0*pA,
        "v_r": -52*mV,
        "i_stim": i*nA,
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
    difference = numpy.around(difference, 1)
    difference = numpy.unique(difference)

    for j in difference:
        stm_values.append(i)
        isi_values.append(j)


df = DataFrame({'variable': stm_values, 'isi': isi_values})
plt.title("Change in inter spike interval by time")
plt.xlabel('Variation of I (nA)')
plt.ylabel('Inter Spike Interval')
plt.scatter(data=df, x='variable', y='isi')
plt.show()
