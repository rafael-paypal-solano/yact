import sys
import os
import pandas
import numpy

if __name__ == "__main__":
    pi_file = sys.argv[1]
    mc_file = sys.argv[2]
    output_file = sys.argv[3]

    pi_dataset = pandas.read_csv(pi_file, sep='|')
    mc_dataset = pandas.read_csv(mc_file, sep='|')
    merged_dataset = pandas.merge(pi_dataset, mc_dataset, on = ('FECHA','MONTO','FUENTE'), suffixes=('_PI', '_MAGYCORP'))
    merged_dataset.to_csv(output_file, sep='|')