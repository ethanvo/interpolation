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

##############################
# Create a "Cell"
##############################

cell = gto.Cell()
# Candidate formula of solid: c, si, sic, bn, bp, aln, alp, mgo, mgs, lih, lif, licl
formula = "lih"
ase_atom = lattice.get_ase_atom(formula)
cell.atom = pyscf_ase.ase_atoms_to_pyscf(ase_atom)
cell.a = ase_atom.cell[:]
cell.unit = 'B'
cell.basis = {'Li': parse_nwchem.load("/burg/berkelbach/users/eav2136/builds/ccgto/basis/gth-hf-rev/cc-pvdz-lc.dat", 'Li'),
              'F': parse_nwchem.load("/burg/berkelbach/users/eav2136/builds/ccgto/basis/gth-hf-rev/cc-pvdz-lc.dat", 'F')}
cell.pseudo = {'Li': "gth-hf-rev-q1",
               'F': "gth-hf-rev"}
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
mydf = df.GDF(cell, kpts=kpts)
mymf.with_df = mydf
ekrhf = mymf.kernel()

mp2_mesh = int(sys.argv[2])
kmesh = [mp2_mesh, mp2_mesh, mp2_mesh]
kpts = cell.make_kpts(kmesh, scaled_center=scaled_center)
mo_energy, mo_coeff = mymf.get_bands(kpts)
mo_energy = np.asarray(mo_energy)
mo_coeff = np.asarray(mo_coeff)

mydf = df.GDF(cell, kpts=kpts)
mydf.build()
nao = cell.nao_nr()
nocc = cell.nelectron // 2
nmo = mo_energy.shape[1]
nvir = nmo - nocc
nkpts = len(kpts)
kconserv = get_kconserv(cell, kpts)
naux = mydf.get_naoaux()

mo_e_o = [mo_energy[k][:nocc] for k in range(nkpts)]
mo_e_v = [mo_energy[k][nocc:] for k in range(nkpts)]
emp2 = 0.0

feri = lib.H5TmpFile()
Lov = feri.create_dataset('Lov', (nkpts, nkpts, naux, nocc, nvir), np.complex128)
bra_start = 0
bra_end = nocc
ket_start = nmo + nocc
ket_end = ket_start + nvir
with h5py.File(mydf._cderi, 'r') as f:
    kptij_lst = f['j3c-kptij'][:]
    tao = []
    ao_loc = None
    for ki, kpti in enumerate(kpts):
        for kj, kptj in enumerate(kpts):
            kpti_kptj = np.array((kpti, kptj))
            Lpq = np.asarray(df._getitem(f, 'j3c', kpti_kptj, kptij_lst))
            mo = np.hstack((mo_coeff[ki], mo_coeff[kj]))
            mo = np.asarray(mo, dtype=np.complex128, order='F')
            if Lpq[0].size != nao**2:
                Lpq = lib.unpack_tril(Lpq).astype(np.complex128)
            out = _ao2mo.r_e2(Lpq, mo, (bra_start, bra_end, ket_start, ket_end), tao, ao_loc)
            Lov[ki, kj] = out.reshape(-1, nocc, nvir)

for ki, kj, ka in loop_kkk(nkpts):
    kb = kconserv[ki, ka, kj]
    eia = mo_e_o[ki][:, None] - mo_e_v[ka]
    ejb = mo_e_o[kj][:, None] - mo_e_v[kb]
    eiajb = lib.direct_sum('ia,jb->iajb', eia, ejb)
    iajb = lib.einsum('Lia,Ljb->iajb', Lov[ki, ka], Lov[kj, kb]) / nkpts
    t2 = np.conj(iajb / eiajb)
    ibja = lib.einsum('Lib,Lja->ibja', Lov[ki, kb], Lov[kj, ka]) / nkpts
    emp2 += 2*lib.einsum('iajb,iajb', t2, iajb).real
    emp2 -=   lib.einsum('iajb,ibja', t2, ibja).real

emp2 /= nkpts
print("MP2 Correlation Energy: ", emp2)
total_energy = ekrhf + emp2

datafile = sys.argv[3]
datadict = {}
datadict['ekrhf'] = ekrhf
datadict['ekmp2'] = emp2
datadict['total_energy'] = total_energy
dump(datadict, f'data/{datafile}')