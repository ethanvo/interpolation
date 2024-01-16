#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from fileutils import load
import berkelplot

interp_data = np.zeros((5, 5))
for scfi in range(2, 9):
    for mpi in range(2, 9):
        data = load(f"data/c_ccpvdz_scf_{scfi}_mp2_{mpi}.json")
        interp_data[scfi - 1, mpi - 1] = data["ekmp2"]

standard_data = interp_data.diagonal()

Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / (Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data[1:], label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[0, 1:], label="SCF 111", linestyle="--", marker="s")
ax.plot(Nk, interp_data[1, 1:], label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 2:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 3:], label="SCF 444", linestyle="-", marker="x")
ax.plot(Nk[3:], interp_data[4, 4:], label="SCF 555", linestyle="-", marker="+")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data[1:], label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[0, 1:], label="SCF 111", linestyle="--", marker="s")
ax.plot(Nk, interp_data[1, 1:], label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 2:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 3:], label="SCF 444", linestyle="-", marker="x")
ax.plot(Nk[3:], interp_data[4, 4:], label="SCF 555", linestyle="-", marker="+")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_nk13.png")

# Plot differences to standard
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / (Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(
    Nk,
    interp_data[0, 1:] - standard_data[1:],
    label="SCF 111",
    linestyle="--",
    marker="s",
)
ax.plot(
    Nk,
    interp_data[1, 1:] - standard_data[1:],
    label="SCF 222",
    linestyle=":",
    marker="^",
)
ax.plot(
    Nk[1:],
    interp_data[2, 2:] - standard_data[2:],
    label="SCF 333",
    linestyle="-.",
    marker="v",
)
ax.plot(
    Nk[2:],
    interp_data[3, 3:] - standard_data[3:],
    label="SCF 444",
    linestyle="-",
    marker="x",
)
ax.plot(
    Nk[3:],
    interp_data[4, 4:] - standard_data[4:],
    label="SCF 555",
    linestyle="-",
    marker="+",
)
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_error.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(
    Nk,
    interp_data[0, 1:] - standard_data[1:],
    label="SCF 111",
    linestyle="--",
    marker="s",
)
ax.plot(
    Nk,
    interp_data[1, 1:] - standard_data[1:],
    label="SCF 222",
    linestyle=":",
    marker="^",
)
ax.plot(
    Nk[1:],
    interp_data[2, 2:] - standard_data[2:],
    label="SCF 333",
    linestyle="-.",
    marker="v",
)
ax.plot(
    Nk[2:],
    interp_data[3, 3:] - standard_data[3:],
    label="SCF 444",
    linestyle="-",
    marker="x",
)
ax.plot(
    Nk[3:],
    interp_data[4, 4:] - standard_data[4:],
    label="SCF 555",
    linestyle="-",
    marker="+",
)
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_error_nk13.png")

# Plot 444, 333, 222 difference to standard
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / (Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(
    Nk,
    interp_data[4, 1:] - standard_data[1:],
    label="SCF 555",
    linestyle="-",
    marker="+",
)
ax.plot(
    Nk[1:],
    interp_data[3, 2:] - standard_data[2:],
    label="SCF 444",
    linestyle="-",
    marker="x",
)
ax.plot(
    Nk[2:],
    interp_data[2, 3:] - standard_data[3:],
    label="SCF 333",
    linestyle="-.",
    marker="v",
)
ax.plot(
    Nk[3:],
    interp_data[1, 4:] - standard_data[4:],
    label="SCF 222",
    linestyle=":",
    marker="^",
)
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444_333_222_error.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4, 5])
Nk = 1 / Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(
    Nk,
    interp_data[4, 1:] - standard_data[1:],
    label="SCF 555",
    linestyle="-",
    marker="+",
)
ax.plot(
    Nk[1:],
    interp_data[3, 2:] - standard_data[2:],
    label="SCF 444",
    linestyle="-",
    marker="x",
)
ax.plot(
    Nk[2:],
    interp_data[2, 3:] - standard_data[3:],
    label="SCF 333",
    linestyle="-.",
    marker="v",
)
ax.plot(
    Nk[3:],
    interp_data[1, 4:] - standard_data[4:],
    label="SCF 222",
    linestyle=":",
    marker="^",
)
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444_333_222_error_nk13.png")
