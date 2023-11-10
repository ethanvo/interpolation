#!/bin/bash
sbatch -J standard_hf_c_ccpvdz_1 --time=5-00:00:00 --mem=187G df_hf_mp2.sh 1 standard_hf_c_ccpvdz_1.json
sbatch -J standard_hf_c_ccpvdz_2 --time=5-00:00:00 --mem=187G df_hf_mp2.sh 2 standard_hf_c_ccpvdz_2.json
sbatch -J standard_hf_c_ccpvdz_3 --time=5-00:00:00 --mem=187G df_hf_mp2.sh 3 standard_hf_c_ccpvdz_3.json
sbatch -J standard_hf_c_ccpvdz_4 --time=5-00:00:00 --mem=187G df_hf_mp2.sh 4 standard_hf_c_ccpvdz_4.json
sbatch -J standard_hf_c_ccpvdz_5 --time=5-00:00:00 --mem=187G df_hf_mp2.sh 5 standard_hf_c_ccpvdz_5.json
