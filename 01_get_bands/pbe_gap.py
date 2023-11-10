#!/usr/bin/env python
import numpy as np
from pyscf.pbc import gto, dft
from pyscf.pbc.tools import pyscf_ase, lattice, get_coulG
from pyscf.gto.basis import parse_nwchem
from pyscf import lib
from pyscf.pbc.lib.kpts_helper import get_kconserv, loop_kkk
from pyscf.pbc.df import df
from pyscf.ao2mo import _ao2mo
import h5py
import sys
from fileutils import load, dump

au2ev = 27.211386245988

##############################
# Create a "Cell"
##############################

cell = gto.Cell()
# Candidate formula of solid: c, si, sic, bn, bp, aln, alp, mgo, mgs, lih, lif, licl
formula = "c"
ase_atom = lattice.get_ase_atom(formula)
cell.atom = pyscf_ase.ase_atoms_to_pyscf(ase_atom)
cell.a = ase_atom.cell[:]
cell.unit = 'B'
cell.basis = {'C': parse_nwchem.load("/Users/ethanvo/builds/ccgto/basis/gth-hf-rev/cc-pvdz-lc.dat", 'C')}
cell.pseudo = "gth-hf-rev"
cell.verbose = 7
cell.build()

##############################
#  K-point SCF 
##############################
datadict = {}
gap = []
for i in range(1, 6):
    kmesh = [i, i, i]
    scaled_center=[0.0, 0.0, 0.0]
    kpts = cell.make_kpts(kmesh, scaled_center=scaled_center)
    mymf = dft.KRKS(cell, kpts=kpts)
    mymf.xc = 'pbe'
    ekrhf = mymf.kernel()
    mo_energy, mo_coeff = mymf.get_bands(kpts)
    nocc = cell.nelectron // 2
    gap.append((mo_energy[0][nocc] - mo_energy[0][nocc-1])*au2ev)

datadict['gap'] = gap
dump(datadict, "pbe_gap_get_bands.json")
