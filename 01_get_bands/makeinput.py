#!/bin/bash/env python

materials = ["c", "lih"]

with open('runall.sh', 'w') as f:
    f.write('#!/bin/zsh\n')
    for material in materials:
        for scfi in range(1, 6):
            for mpi in range(5, 6):
                key = '{}_ccpvdz_scf_{}_mp2_{}'.format(material, scfi, mpi)
                f.write('python3 {}_df_dft_mp2.py {} {} {}.json 1> {}.out 2> {}.err\n'.format(material, scfi, mpi, key, key, key))
