#!/bin/bash/env python
with open('runall.sh', 'w') as f:
    f.write('#!/bin/zsh\n')
    for scfi in range(1, 6):
        for mpi in range(5, 6):
            key = 'c_ccpvdz_scf_{}_mp2_{}'.format(scfi, mpi)
            f.write('python3 df_dft_mp2.py {} {} {}.json 1> {}.out 2> {}.err\n'.format(scfi, mpi, key, key, key))
