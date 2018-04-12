import sys
import os
import pandas
import numpy
index_columns = ['FUENTE', 'FECHA', 'MONTO']

def output_diff(output_file, df1, df2):
    diff = df1[~df1.index.isin(df2.index)]
    diff.to_csv(output_file, sep='|')
    return diff

def read_csv(input_file):
    dataset = pandas.read_csv(input_file, sep='|')
    dataset.set_index(index_columns, inplace = True)
    return dataset

if __name__ == "__main__":
    pi_file = sys.argv[1]
    mc_file = sys.argv[2]
    output_folder = sys.argv[3]
    pi_dataset = read_csv(pi_file)
    mc_dataset = read_csv(mc_file)

    pi_minus_mc = output_diff(output_folder + "/pi_minus_mc.csv", pi_dataset, mc_dataset)
    mc_minus_pi = output_diff(output_folder + "/mc_minus_pi.csv", mc_dataset, pi_dataset)
    
    print("pi: %d" % (len(pi_dataset)))
    print("mc: %d" % (len(mc_dataset)))
    print("pi - mc: %d" % (len(pi_dataset) - len(pi_minus_mc)))
    print("mc - pi: %d" % (len(mc_dataset) - len(mc_minus_pi)))