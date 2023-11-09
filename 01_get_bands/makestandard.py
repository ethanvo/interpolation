#!/bin/bash/env python
with open('standardrunall.sh', 'w') as f:
    f.write('#!/bin/zsh\n')
    for scfi in range(1, 5):
        key = 'standard_c_ccpvdz_dft_mp2_{}'.format(scfi)
        f.write('python3 standard_dft_mp2.py {} {}.json 1> {}.out 2> {}.err\n'.format(scfi, key, key, key))
