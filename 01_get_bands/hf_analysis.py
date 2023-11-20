#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from fileutils import load
import berkelplot
import matplotlib

hf_data = np.zeros(4)
for i in range(2, 6):
    data = load("data/standard_hf_c_ccpvdz_{}.json".format(i))
    hf_data[i - 2] = data["ekmp2"]


Nk = np.asarray([2, 3, 4, 5])
Nk = 1/(Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, hf_data, marker="o")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.13)
plt.savefig("c_ccpvdz_hf_mp2_nk.png")

Nk = np.asarray([2, 3, 4, 5])
Nk = 1/Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, hf_data, marker="o")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.55)
plt.savefig("c_ccpvdz_hf_mp2_nk13.png")
