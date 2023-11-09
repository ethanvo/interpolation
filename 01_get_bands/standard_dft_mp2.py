#!/usr/bin/env python
import numpy as np
from pyscf.pbc import gto, dft, df
from pyscf.pbc.tools import pyscf_ase, lattice, get_coulG
from pyscf.gto.basis import parse_nwchem
from pyscf.pbc.mp.kmp2 import KRMP2
from pyscf import lib
import h5py
import sys
from fileutils import load, dump

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

##############################
#  K-point MP2
##############################
mymp = KRMP2(mymf)
mydf = df.GDF(cell, kpts)
mymp._scf.with_df = mydf
mymp.with_df_ints = True
ekmp2, t2 = mymp.kernel()

total_energy = ekrhf + ekmp2
datafile = sys.argv[2]
datadict = {}
datadict['ekrhf'] = ekrhf
datadict['ekmp2'] = ekmp2
datadict['total_energy'] = total_energy
dump(datadict, f'data/{datafile}')
