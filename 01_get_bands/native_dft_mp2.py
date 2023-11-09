#!/usr/bin/env python
import numpy as np
from pyscf.pbc import gto, dft, df
from pyscf.pbc.tools import pyscf_ase, lattice, get_coulG
from pyscf.gto.basis import parse_nwchem
from pyscf import lib
from pyscf.pbc.lib.kpts_helper import get_kconserv, KptsHelper
from pyscf.pbc.mp.kmp2 import KRMP2
import h5py
from fileutils import load, dump 
import sys

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
scf_mesh = int(sys.argv[1])
kmesh = [scf_mesh, scf_mesh, scf_mesh]
scaled_center=[0.0, 0.0, 0.0]
kpts = cell.make_kpts(kmesh, scaled_center=scaled_center)
mymf = dft.KRKS(cell, kpts=kpts)
mymf.xc = 'pbe'
ekrhf = mymf.kernel()

mp2_mesh = int(sys.argv[2])
kmesh = [mp2_mesh, mp2_mesh, mp2_mesh]
kpts_interp = cell.make_kpts(kmesh, scaled_center=scaled_center)
mo_energy, mo_coeff = mymf.get_bands(kpts_interp)
mo_energy = np.asarray(mo_energy)
mo_coeff = np.asarray(mo_coeff)
mo_occ_dtype = mymf.mo_occ[0].dtype
mo_occ = np.zeros_like(mo_energy, dtype=mo_occ_dtype)
nocc = cell.nelectron // 2
mo_occ[:, :nocc] = 2.0

mydf = df.GDF(cell, kpts=kpts_interp)

##############################
#  MP2
##############################
mymp = KRMP2(mymf, frozen=None, mo_coeff=mo_coeff, mo_occ=mo_occ)
mymp.with_df_ints = True
mymp._scf.with_df = mydf
mymp.kpts = kpts_interp
mymp.mo_energy = mo_energy
mymp.nkpts = len(kpts_interp)
mymp.khelper = KptsHelper(cell, kpts_interp)
ekmp2, t2 = mymp.kernel()
total_energy = ekrhf + ekmp2

datafile = sys.argv[3]
datadict = {}
datadict['ekrhf'] = ekrhf
datadict['ekmp2'] = ekmp2
datadict['total_energy'] = total_energy
dump(datadict, f'data/{datafile}')
