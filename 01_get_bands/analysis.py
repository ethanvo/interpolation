#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from fileutils import load
import berkelplot
import matplotlib

interp_data = np.zeros((4, 3))
standard_data = np.zeros(3)
for scfi in range(1, 5):
    for mpi in range(2, 5):
        data = load(f"data/c_ccpvdz_scf_{scfi}_mp2_{mpi}.json")
        interp_data[scfi-1, mpi-2] = data["ekmp2"]

for scfi in range(2, 5):
    data = load(f"data/standard_c_ccpvdz_dft_mp2_{scfi}.json")
    standard_data[scfi-2] = data["ekmp2"]

Nk = np.asarray([2, 3, 4])
Nk = 1/(Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data, label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[0], label="SCF 111", linestyle='--', marker="s")
ax.plot(Nk, interp_data[1], label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 1:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 2:], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4])
Nk = 1/Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data, label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[0], label="SCF 111", linestyle='--', marker="s")
ax.plot(Nk, interp_data[1], label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 1:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 2:], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_nk13.png")

# Plot differences to standard
Nk = np.asarray([2, 3, 4])
Nk = 1/(Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, interp_data[0]-standard_data, label="SCF 111", linestyle='--', marker="s")
ax.plot(Nk, interp_data[1]-standard_data, label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 1:]-standard_data[1:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 2:]-standard_data[2:], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_error.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4])
Nk = 1/Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, interp_data[0]-standard_data, label="SCF 111", linestyle='--', marker="s")
ax.plot(Nk, interp_data[1]-standard_data, label="SCF 222", linestyle=":", marker="^")
ax.plot(Nk[1:], interp_data[2, 1:]-standard_data[1:], label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk[2:], interp_data[3, 2:]-standard_data[2:], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_error_nk13.png")

# Plot 444 against standard
Nk = np.asarray([2, 3, 4])
Nk = 1/(Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data, label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[3], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4])
Nk = 1/Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, standard_data, label="DFT-MP2", marker="o", color="black")
ax.plot(Nk, interp_data[3], label="SCF 444", linestyle="-", marker="x")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Corr. Energy (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444_nk13.png")

# Plot 444, 333, 222 difference to standard
Nk = np.asarray([2, 3, 4])
Nk = 1/(Nk**3)
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, interp_data[3]-standard_data, label="SCF 444", linestyle="-", marker="x")
ax.plot(Nk, interp_data[2]-standard_data, label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk, interp_data[1]-standard_data, label="SCF 222", linestyle=":", marker="^")
ax.set_xlabel(r"$1/N_k$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.13)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444_333_222_error.png")

# Same plot but 1/Nk
Nk = np.asarray([2, 3, 4])
Nk = 1/Nk
size = berkelplot.fig_size(n_row=2, n_col=1)
fix, ax = plt.subplots(1, 1, figsize=size)
ax.plot(Nk, interp_data[3]-standard_data, label="SCF 444", linestyle="-", marker="x")
ax.plot(Nk, interp_data[2]-standard_data, label="SCF 333", linestyle="-.", marker="v")
ax.plot(Nk, interp_data[1]-standard_data, label="SCF 222", linestyle=":", marker="^")
ax.set_xlabel(r"$N_k^{-1/3}$")
ax.set_ylabel("Interpolation Error (Ha)")
ax.set_xlim(0, 0.55)
ax.legend()
plt.savefig("c_ccpvdz_scf_mp2_444_333_222_error_nk13.png")
