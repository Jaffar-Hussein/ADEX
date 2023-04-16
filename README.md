**GURA Jaffar**


**REPORT**

**Modelling of neuronal interactions at the claustrum level**

**[LABORATORY: UMR9197 NEUROPSI SACLAY FRANCE](https://neuropsi.cnrs.fr)**

**LABORATORY DIRECTOR: Mr. ROUYER Francois**

**TEAM: Computational Neuroscience**

**ACADEMIC SUPERVISOR: Prof. JACQUIR Sabir**

**INTERNSHIP SUPERVISOR: Prof. PANANCEAU Marc**

**ADDRESSEE: 151 Centre CEA Saclay 91400 SACLAY FRANCE**

**2021/2022**

# Table of Contents

[Abbreviations](#abbreviations)

[Abstract](#abstract)

[I) INTRODUCTION](#introduction)

[II) Methods](#methods)

[1. Adaptive Exponential Integrate Model
](#adaptive-exponential-integrate-model)

[2. Testing the relative effects of variables to the Adex Model
](#testing-the-relative-effects-of-variables-to-the-adex-model)

[3. Modelling Spike Trains from Experimental Data
](#modelling-spike-trains-from-experimental-data)

[III) Results and Discussions
](#results-and-discussions)

[I) Interspike Intervals with a variation of the τ ω
](#interspike-intervals-with-a-variation-of-the-τ-ω)

[II) Interspike Intervals with a variation of the values of b](#interspike-intervals-with-a-variation-of-the-values-of-b)

[III) Interspike Intervals with a variation of the a
](#interspike-intervals-with-a-variation-of-the-a)

[IV) Interspike Intervals with the variation of the injected current
](#interspike-intervals-with-the-variation-of-the-injected-current)

[V) Models from Experimental Data
](#models-from-experimental-data)

[VI) Conclusions ](#conclusions)

[Bibliography ](#Bibliography)



# Abbreviations

VIP -- Vasoactive Intestinal Peptides

PV - Parvalbumin

SOM - Somatostatin

NPY - Neuropeptide Y

ADEX -- Adaptive Exponential Integrate and Fire Model

ISI -- Interspike interval

tau- Membrane time constant

# Abstract

Several studies have modelled the dynamics of neurons and not a lot
specifically target the neurons of the claustrum. The claustrum neurons
are hampered by not having an agreed defined boundary. In our
internship, we study several models for neurons in general and see the
effect of the modulation of their parameters. We then simulate
experimental data to reproduce the neuron dynamics observed.

# INTRODUCTION

The claustrum is a thin sheet of grey matter located in the forebrain,
extending rostrocaudally along with the striatum and situated between
the insula and putamen (Smith, Lee and Jackson, 2020). It is the most
densely interconnected region of the brain (Graf *et al.*, 2020). The
claustrum is composed of both the spiny stellate projection neurons and
a variety of aspiny interneurons that can be differentiated by the
expression of various peptides and calcium-binding proteins such as PV,
VIP, SOM, NPY and others (Smith, Lee and Jackson, 2020). Due to the high
connection of the claustrum and other parts of the brain, it is thought
to take part in higher cognitive functions where it integrates
information and hence supports the consciousness (Crick and Koch, 2005).
The claustrum is also believed to take part in attention and resilience
from distraction (Atlan *et al.*, 2018). It has also been linked to
sleep (Liu *et al.*, 2019) and impulsivity(Norimoto *et al.*, 2020).

The claustrum projection neurons and interneurons can be distinguished
from each other based on their intrinsic electrical properties. The
projection neurons can be subdivided into 5 subclasses based on their
intrinsic electrical properties. This makes a total of 8 subclasses of
claustrum neurons(Graf *et al.*, 2020).

A neuron fires when it gets input from other sources. The firing of a
neuron produces an action potential (spike), which is an abrupt
transient change of the membrane voltage that propagates to other
neurons(Izhikevich, 2007). There are several models with different
parameters allowing the simulation of neuron dynamics. In the team, we
worked with the Adex model which is a relatively simple model with two
differential equations one for the voltage with respect to time and the
other for the adaptation variable with respect to time. The model shows
the evolution of the voltage in time when a current I is injected (Naud
*et al.*, 2008).

This internship aims to reproduce the dynamics of claustrum neurons
observed in the experimental works (Graf *et al.*, 2020). First, we
simulated the ADEX model in order to understand the influence of
different parameters on the Interspike interval then we reproduced
qualitatively some parameters of the neurons observed experimentally.

# Methods

All simulations were done in the Brian2 neural simulator and Python 3
programming language.

### Adaptive Exponential Integrate Model

This is a model of two differential equations that model the evolution
of membrane potential V when a certain current I is injected into the
system.

$$C\frac{dV}{dt} = \  - g_{l}\left( V - E_{L} \right) + g_{L}*\ \mathrm{\Delta}_{T}\exp\left( \frac{V - V_{T}}{\mathrm{\Delta}_{T}} \right) - \omega + Ι$$

Equation Adaptation

$$\tau_{\omega}\frac{d\omega}{dt} = a\left( V - E_{L} \right) - \omega$$

Equation Adaptation Current

Where :

$C$ = Membrane Capacitance

V = Membrane Potential

g~L~ = Leak Conductance

E~L~ = Resting Potential

V~T~ = Threshold Potential

ω = Adaptation Variable

I = Synaptic Current

τ ~ω~ = Time constant

∆~T\ =~ Threshold Slope Factor

a = Subthreshold Adaptation

When the current drives the potential beyond the threshold V~T~ this
leads to the positive feedback that drives an upswing of the action
potential. The upswing is stopped by a reset threshold that we fix, and
the action potential is replaced by a reset condition (Equation 1)(Naud
*et al.*, 2008).

$$if\ V > V_{T}\ then\ \begin{Bmatrix}
V \rightarrow V_{r} \\
\omega\  \rightarrow {\omega\ }_{r} = \omega\  + b \\
\end{Bmatrix}$$

Equation Reset Condition for the ADEX Model

Where:

b = Spike triggered adaptation

V~r~ = Reset Potential

The membrane potential is reset to V reset whereas the adaptation
variable is reset to the w~r~ which is the adaptation variable plus a
fixed amount b. The adaptation variable accumulates during the spike
train whereas the membrane potential does not.

The nine parameters can be divided into bifurcation and scaling
parameters. The scaling parameters are involved for scaling the time
axis. The five scaling parameters are the total capacitance (C), total
leak conductance (g~L~ ), effective rest potential (E~L~ ), threshold
slope factor (∆~T~ ), effective threshold potential (V~T~ ).

The remaining four parameters are bifurcation parameters and are
directly related to the conductance a, the time constant τw,the spike
triggered adaptation b, and the rest potential Vr. The modification of
these four parameters results in changes in the firing patterns.

### Testing the relative effects of variables to the Adex Model

To test the effect of different parameters on the evolution of the spike
train we simulated the firing of a neuron while adjusting for the value
of interest. While this was happening, we fixed the rest of the
variables to pre-defined control in which was our starting point for the
experiment as :

C = 200 pF

g~L~ = 10 nS

E~L~ = -65mV

V~T~ = -55 mV

I = .120nA

τ ~ω~ = 500 ms

dt = 5 mV

a = 2 pA

b = 10 pA

V~r~ = -52 mV

We varied the $a,\ b\ ,input\ current\  tau$.We recorded the spike
train and the ISI for the variable parameters while leaving the rest of
the parameters to remain the same as the control. We set the threshold
at -40mV and the refractory period to be 5ms. The experiment ran for 4s
for each simulation, and we took the value from 500ms to 4000ms to avoid
any bias at the beginning of the spike train.

### Modelling Spike Trains from Experimental Data

We modelled the neurons according to the intrinsic electrical properties
that we fixed into the Adex model derived from the classification of the
rat claustrum (Graf *et al.*, 2020). The Adex model (Figure 1), has 9
variables and we got 4 variables from the experimental data, that is the
membrane potential, the input current, the threshold, and the leak
conductance.

We fixed the variables that we got from the paper into the model and
modulated the rest of the variables to try and simulate the experimental
spike trains.

# Results and Discussions

The Adex model has been simulated with a variation of these parameters :

a , b , synaptic current , and τ ~ω~ ,Then the Interspike intervals have
been computed in order to look at the influence of these different
parameters on the frequency of the spikes.

### Interspike Intervals with a variation of the τ ~ω~

<img width="718" alt="image1" src="https://user-images.githubusercontent.com/57854451/232287973-9c6a5e15-51ed-4813-95a4-568c21236a4f.png">


Figure Change of ISI for variation of tau (ms)

In Figure 3 we vary the τ ~ω~ from 0ms to 1000ms and where a is 10 nS, b
is fixed at 10nS, and synaptic current is fixed at .120nA.

At point a in the graph the τ ~ω~ is 200ms we observe spike train with a
high frequency and regular ISI. With increase to point b of τ ~ω~ is
600ms we observe six values of ISI and hence an irregular spike train.
The third mark is at 1000ms we observe three distinct values of ISI and
hence more regular than b.

### Interspike Intervals with a variation of the values of b

In Figure 4 we vary the b from 0 pA to 25 pA and where a is 10 nS, τ ~ω~
is fixed at 500ms, and synaptic current is fixed at .120nA.

At point a in the graph the b is at 7 pA we observe spike train with a
high frequency and regular ISI. With increase to point b of b is 17 pA
we observe 4 values of ISI and hence an irregular spike train. The third
mark is at 27 pA we observe two distinct values of ISI and hence more
regular than b.

<img width="648" alt="image2" src="https://user-images.githubusercontent.com/57854451/232287895-6f91fabe-1c68-4218-8dfc-4188fb407a59.png">




Figure Variation of ISI with b (pA)

### Interspike Intervals with a variation of the a

In Figure 5 we vary the a from 0nS to 10nS and where b is 2nS, τ ~ω~ is
fixed at 500ms, and synaptic current is fixed at .120nA.

At point (a) in the graph the a is at 1 nS we observe spike train with a
high frequency and regular ISI. With increase to point (b) of b is 4nS
we observe 4 values of ISI and hence an irregular spike train. The third
mark is at 6 nS we observe three distinct values of ISI and hence more
regular than (b).
![image3](https://user-images.githubusercontent.com/57854451/232287845-6ccc4473-3da7-44f4-98aa-deb6dd18aa1d.png)


Figure Variation of ISI for a (nS)

### Interspike Intervals with the variation of the injected current

![image4](https://user-images.githubusercontent.com/57854451/232287755-e1eddb00-0f2b-4973-9cce-da6ab4b39fe5.png)



Figure Variation of ISI (s) with Injected current (pA)

In Figure 6 we vary the synaptic current from 0.05pA to 0.250pA and
where b is 2nS, τ ~ω~ is fixed at 500ms, and a is 10 nS.

At point (a) in the graph the synaptic current is at 0.08 pA we observe
spike train with a low frequency and an irregular spike train. With
increase to point (b) with synaptic current as 0.150 pA we a high
frequency spike train compared to (a) with a regular ISI. The third mark
is at 0.250 pA the frequency increases from the one at (b) and the ISI
remains regular.

## Models from Experimental Data

The data divides the neurons of the claustrum into the two major groups
interneurons and projection neurons and further subdivides the
projection neurons into five subgroups according to the shape of their
spike trains.(Graf *et al.*, 2020). The data in figure on the left are
the five sib-divisions of projections and one interneuron whereas the
figures on the right are the pre-liminary results obtained from our
simulations. They show a bit of difference but don't much up exactly to
the experimental data, this discrepancy is caused by lack of majority of
the variables considered in the ADEX model from the experimental data.

<img width="1113" alt="Screenshot 2023-04-16 at 10 57 30" src="https://user-images.githubusercontent.com/57854451/232288070-41328f5c-84d6-4bb6-87de-dece78c436f5.png">


<img width="385" alt="image6" src="https://user-images.githubusercontent.com/57854451/232288027-bd3cbb14-650a-446c-a83b-fd12f9e0912a.png">


Figure Classification of claustrum neurons
(a) the experimental spike trains (Graf et al., 2020) (b) the
values of our simulations with data from experiments on mice (Graf et
al., 2020)



# Conclusions

We grouped the neurons of the claustrum according to their electrical
properties and their expression of different peptides. In total we
arrived at 8 distinct subgroups of the claustrum inter-neurons and also
obtained preliminary results in our simulations from experimental data.
In addition, I learnt different neuron models with increased complexity
till I arrived to the Adex model that our team was using for modelling
of the claustrum neurons.

The rest of the experimental data and all simulations can be accessed
through the GitHub repository
<https://github.com/Jaffar-Hussein/Neurone-Models>

# Bibliography

Sciences Atlan, G. *et al.* (2018) 'The Claustrum Supports Resilience to
Distraction', *Current Biology*, 28(17), pp. 2752-2762.e7.
doi:10.1016/j.cub.2018.06.068.

Crick, F.C. and Koch, C. (2005) 'What is the function of the
claustrum?', *Philosophical transactions of the Royal Society of London.
Series B, Biological sciences*, 360(1458), pp. 1271--1279.
doi:10.1098/rstb.2005.1661.

Graf, M. *et al.* (2020) 'Identification of Mouse Claustral Neuron Types
Based on Their Intrinsic Electrical Properties', *eneuro*, 7(4), p.
ENEURO.0216-20.2020. doi:10.1523/ENEURO.0216-20.2020.

Izhikevich, E.M. (2007) *Dynamical systems in neuroscience: the geometry
of excitability and bursting*. Cambridge, Mass: MIT press (Computational
neuroscience).

Liu, J. *et al.* (2019) 'The Claustrum-Prefrontal Cortex Pathway
Regulates Impulsive-Like Behavior', *The Journal of Neuroscience*,
39(50), pp. 10071--10080. doi:10.1523/JNEUROSCI.1005-19.2019.

Naud, R. *et al.* (2008) 'Firing patterns in the adaptive exponential
integrate-and-fire model', *Biological Cybernetics*, 99(4--5), pp.
335--347. doi:10.1007/s00422-008-0264-7.

Norimoto, H. *et al.* (2020) 'A claustrum in reptiles and its role in
slow-wave sleep', *Nature*, 578(7795), pp. 413--418.
doi:10.1038/s41586-020-1993-6.

Smith, J.B., Lee, A.K. and Jackson, J. (2020) 'The claustrum', *Current
Biology*, 30(23), pp. R1401--R1406. doi:10.1016/j.cub.2020.09.069.

[^1]: The experimental spike trains obtained from (Graf *et al.*, 2020)


