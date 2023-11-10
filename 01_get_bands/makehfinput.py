#!/bin/bash/env python
with open('runall.sh', 'w') as f:
    f.write('#!/bin/bash\n')
    for scfi in range(1, 6):
        key = 'standard_hf_c_ccpvdz_{}'.format(scfi)
        f.write('sbatch -J {} --time=5-00:00:00 --mem=187G df_hf_mp2.sh {} {}.json\n'.format(key, scfi, key, key, key))
