#!/usr/bin/env python3
from fileutils import load
import numpy as np
import berkelplot
import matplotlib.pyplot as plt

def get_interp_data(material, scf):
    data = [load(f"data/{material}_ccpvdz_scf_{scf}_mp2_{mpi}.json")["ekmp2"] for mpi in range(2, 9)]
    return np.asarray(data)

def get_standard_data(material):
    data = [load(f"data/{material}_ccpvdz_scf_{i}_mp2_{i}.json")["ekmp2"] for i in range(2, 9)]
    return np.asarray(data)

materials = ["c", "lif"]
Nk = np.arange(2, 9)
Nk_inv = 1 / (Nk**3)
Nk_inv_13 = 1 / Nk

size = berkelplot.fig_size(n_row=2, n_col=1)
markers = ["o", "s", "D", "v", "^", "p", "*", "h"]  # List of marker styles

for material in materials:
    fig, ax = plt.subplots(1, 1, figsize=size)
    ax.plot(Nk_inv, get_standard_data(material), label="DFT-MP2", marker="o", color="black")
    for i in Nk:
        ax.plot(Nk_inv[i-2:], get_interp_data(material, i)[i-2:], label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$1/N_k$")
    ax.set_ylabel("Corr. Energy (Ha)")
    ax.set_xlim(0, 0.13)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2.png")

    fig, ax = plt.subplots(1, 1, figsize=size)
    ax.plot(Nk_inv_13, get_standard_data(material), label="DFT-MP2", marker="o", color="black")
    for i in Nk:
        ax.plot(Nk_inv_13[i-2:], get_interp_data(material, i)[i-2:], label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$N_k^{-1/3}$")
    ax.set_ylabel("Corr. Energy (Ha)")
    ax.set_xlim(0, 0.55)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_nk13.png")

    fig, ax = plt.subplots(1, 1, figsize=size)
    ax.plot(Nk_inv, get_standard_data(material), label="DFT-MP2", marker="o", color="black")
    for i in Nk:
        ax.plot(Nk_inv, get_interp_data(material, i), label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$1/N_k$")
    ax.set_ylabel("Corr. Energy (Ha)")
    ax.set_xlim(0, 0.13)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_all.png")
    
    fig, ax = plt.subplots(1, 1, figsize=size)
    ax.plot(Nk_inv_13, get_standard_data(material), label="DFT-MP2", marker="o", color="black")
    for i in Nk:
        ax.plot(Nk_inv_13, get_interp_data(material, i), label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$N_k^{-1/3}$")
    ax.set_ylabel("Corr. Energy (Ha)")
    ax.set_xlim(0, 0.55)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_nk13_all.png")

    # Error plots
    fig, ax = plt.subplots(1, 1, figsize=size)
    for i in Nk:
        ax.plot(Nk_inv[i-2:], get_interp_data(material, i)[i-2:] - get_standard_data(material)[i-2:], label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.plot((0, 0.13), (0, 0), linestyle="--", color="black")
    ax.set_xlabel(r"$1/N_k$")
    ax.set_ylabel("Corr. Energy Error (Ha)")
    ax.set_xlim(0, 0.13)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_error.png")

    fig, ax = plt.subplots(1, 1, figsize=size)
    for i in Nk:
        ax.plot(Nk_inv_13[i-2:], get_interp_data(material, i)[i-2:] - get_standard_data(material)[i-2:], label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.plot((0, 0.55), (0, 0), linestyle="--", color="black")
    ax.set_xlabel(r"$N_k^{-1/3}$")
    ax.set_ylabel("Corr. Energy Error (Ha)")
    ax.set_xlim(0, 0.55)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_nk13_error.png")

    fig, ax = plt.subplots(1, 1, figsize=size)
    for i in Nk:
        ax.plot(Nk_inv, get_interp_data(material, i) - get_standard_data(material), label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$1/N_k$")
    ax.set_ylabel("Corr. Energy Error (Ha)")
    ax.set_xlim(0, 0.13)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_all_error.png")
    
    fig, ax = plt.subplots(1, 1, figsize=size)
    for i in Nk:
        ax.plot(Nk_inv_13, get_interp_data(material, i) - get_standard_data(material), label=f"SCF {i}{i}{i}", marker=markers[i - 2])
    ax.set_xlabel(r"$N_k^{-1/3}$")
    ax.set_ylabel("Corr. Energy Error (Ha)")
    ax.set_xlim(0, 0.55)
    ax.legend()
    plt.savefig(f"figures/{material}_ccpvdz_scf_mp2_nk13_all_error.png")
