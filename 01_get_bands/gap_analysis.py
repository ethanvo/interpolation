#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from fileutils import load
import berkelplot
import matplotlib

data = load("pbe_gap_get_bands.json")
energies = data["gap"]
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fig, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, energies[1:], marker="o", color="black")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel(r"$E_{\mathrm{gap}}$ (eV)")
ax.set_xlim(0, 0.55)
plt.tight_layout()
plt.savefig("pbe_gap_nk13_get_bands.png")

Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / (Nk ** 3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fig, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, energies[1:], marker="o", color="black")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel(r"$E_{\mathrm{gap}}$ (eV)")
ax.set_xlim(0, 0.13)
plt.tight_layout()
plt.savefig("pbe_gap_nk_get_bands.png")

