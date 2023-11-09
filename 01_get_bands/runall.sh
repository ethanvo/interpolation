#!/bin/zsh
python3 df_dft_mp2.py 1 5 c_ccpvdz_scf_1_mp2_5.json 1> c_ccpvdz_scf_1_mp2_5.out 2> c_ccpvdz_scf_1_mp2_5.err
python3 df_dft_mp2.py 2 5 c_ccpvdz_scf_2_mp2_5.json 1> c_ccpvdz_scf_2_mp2_5.out 2> c_ccpvdz_scf_2_mp2_5.err
python3 df_dft_mp2.py 3 5 c_ccpvdz_scf_3_mp2_5.json 1> c_ccpvdz_scf_3_mp2_5.out 2> c_ccpvdz_scf_3_mp2_5.err
python3 df_dft_mp2.py 4 5 c_ccpvdz_scf_4_mp2_5.json 1> c_ccpvdz_scf_4_mp2_5.out 2> c_ccpvdz_scf_4_mp2_5.err
python3 df_dft_mp2.py 5 5 c_ccpvdz_scf_5_mp2_5.json 1> c_ccpvdz_scf_5_mp2_5.out 2> c_ccpvdz_scf_5_mp2_5.err
