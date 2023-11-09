#!/bin/zsh
python3 standard_dft_mp2.py 1 standard_c_ccpvdz_dft_mp2_1.json 1> standard_c_ccpvdz_dft_mp2_1.out 2> standard_c_ccpvdz_dft_mp2_1.err
python3 standard_dft_mp2.py 2 standard_c_ccpvdz_dft_mp2_2.json 1> standard_c_ccpvdz_dft_mp2_2.out 2> standard_c_ccpvdz_dft_mp2_2.err
python3 standard_dft_mp2.py 3 standard_c_ccpvdz_dft_mp2_3.json 1> standard_c_ccpvdz_dft_mp2_3.out 2> standard_c_ccpvdz_dft_mp2_3.err
python3 standard_dft_mp2.py 4 standard_c_ccpvdz_dft_mp2_4.json 1> standard_c_ccpvdz_dft_mp2_4.out 2> standard_c_ccpvdz_dft_mp2_4.err
