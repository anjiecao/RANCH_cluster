
import argparse
import os
import pandas as pd
import ipdb

def populate_dir(args):
    
    # first empty param dir
    param_path = 'RANCH_cluster/MIT_tools/param_dir/'
    test_param_path = "RANCH_cluster/MIT_tools/test_param_dir/"
    files = os.listdir(param_path)

    for f in files:
        os.remove(param_path + f)

    # read csv
    param_info = pd.read_csv(args.param_info_path)

    # get one row and create csv in param_dir
    for index, row in param_info.iterrows():
        if index in [2,4,5,6,7,8,9,16,17,18,20,21,22,24,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,138,160]:
            param_info.iloc[[index]].to_csv(param_path + str(index) + '.csv', index=False)

    # populate test dir with 3 random rows
    for index, row in param_info.sample(n=0).iterrows():
        param_info.iloc[[index]].to_csv(test_param_path + str(index) + '.csv', index=False)
        

if __name__ == '__main__':
    print('entered main script')
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    args = parser.parse_args()
    populate_dir(args)