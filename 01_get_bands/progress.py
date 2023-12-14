#!/usr/bin/env python3
import os

materials = ["c", "lif"]
# open file progress.txt to write as f
f = open("progress.txt", "w")
for material in materials:
    for i in range(1, 11):
        for j in range(1, 11):
            # Check if "{}_ccpvdz_scf_{}_mp2_{}.json".format(material, i, j) doesn't exist, write filename to f
            if not os.path.exists("data/{}_ccpvdz_scf_{}_mp2_{}.json".format(material, i, j)):
                f.write("sbatch -J {}_ccpvdz_scf_{}_mp2_{} --time=5-00:00:00 --mem=716800 {}_df_dft_mp2.sh {} {} {}_ccpvdz_scf_{}_mp2_{}.json\n".format(material, i, j, material, i, j, material, i, j))
f.close()