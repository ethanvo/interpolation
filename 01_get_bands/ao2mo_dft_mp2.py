#!/usr/bin/env python
import numpy as np
from pyscf.pbc import gto, dft, df
from pyscf.pbc.tools import pyscf_ase, lattice, get_coulG
from pyscf.gto.basis import parse_nwchem
from pyscf import lib
from pyscf.pbc.lib.kpts_helper import get_kconserv, loop_kkk
from fileutils import load, dump
import h5py
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
kpts = cell.make_kpts(kmesh, scaled_center=scaled_center)
mo_energy, mo_coeff = mymf.get_bands(kpts)
mo_energy = np.asarray(mo_energy)
mo_coeff = np.asarray(mo_coeff)

mydf = df.GDF(cell, kpts=kpts)
nocc = cell.nelectron // 2
nmo = mo_energy.shape[1]
nvir = nmo - nocc
nkpts = len(kpts)
kconserv = get_kconserv(cell, kpts)

mo_e_o = [mo_energy[k][:nocc] for k in range(nkpts)]
mo_e_v = [mo_energy[k][nocc:] for k in range(nkpts)]
emp2 = 0.0

ao2mo = mydf.ao2mo

for ki, kj, ka in loop_kkk(nkpts):
    kb = kconserv[ki, ka, kj]
    ci = mo_coeff[ki][:, :nocc]
    cj = mo_coeff[kj][:, :nocc]
    ca = mo_coeff[ka][:, nocc:]
    cb = mo_coeff[kb][:, nocc:]
    eia = mo_e_o[ki][:, None] - mo_e_v[ka]
    ejb = mo_e_o[kj][:, None] - mo_e_v[kb]
    eiajb = lib.direct_sum('ia,jb->iajb', eia, ejb)
    iajb = ao2mo((ci, ca, cj, cb), (kpts[ki], kpts[ka], kpts[kj], kpts[kb]), compact=False).reshape(nocc, nvir, nocc, nvir) / nkpts
    t2 = np.conj(iajb / eiajb)
    ibja = ao2mo((ci, cb, cj, ca), (kpts[ki], kpts[kb], kpts[kj], kpts[ka]), compact=False).reshape(nocc, nvir, nocc, nvir) / nkpts
    emp2 += 2*lib.einsum('iajb,iajb', t2, iajb).real
    emp2 -=   lib.einsum('iajb,ibja', t2, ibja).real

emp2 /= nkpts
total_energy = ekrhf + emp2

datafile = sys.argv[3]
datadict = {}
datadict['ekrhf'] = ekrhf
datadict['ekmp2'] = emp2
datadict['total_energy'] = total_energy
dump(datadict, f'data/{datafile}')
