#!/bin/bash/env python

materials = ["c", "lih"]

with open('runall.sh', 'w') as f:
    f.write('#!/bin/bash\n')
    for material in materials:
        for scfi in range(2, 11):
            for mpi in range(2, 11):
                key = '{}_ccpvdz_scf_{}_mp2_{}'.format(material, scfi, mpi)
                f.write('sbatch -J {} --time=5-00:00:00 --mem=187G {}_df_dft_mp2.sh {} {} {}.json\n'.format(key, material, scfi, mpi key))