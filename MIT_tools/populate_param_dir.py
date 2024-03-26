
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
        #if index in [3, 6, 30, 33, 36, 39, 42, 45, 48, 51, 52, 54, 55, 57, 58, 60, 64, 138, 147, 148, 151, 153, 168, 199, 201]:
        param_info.iloc[[index]].to_csv(param_path + str(index) + '.csv', index=False)

    # populate test dir with 3 random rows
    for index, row in param_info.sample(n=3).iterrows():
        param_info.iloc[[index]].to_csv(test_param_path + str(index) + '.csv', index=False)
        

if __name__ == '__main__':
    print('entered main script')
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    args = parser.parse_args()
    populate_dir(args)