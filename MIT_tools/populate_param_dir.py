
import argparse
import os
import pandas as pd

def populate_dir(args):
    
    # first empty param dir
    param_path = 'RANCH_cluster/MIT_tools/param_dir/'
    files = os.listdir(param_path)

    for f in files:
        os.remove(param_path + f)

    # read csv
    param_info = pd.read_csv(args.param_info_path)

    # get one row and create csv in param_dir
    for i in range(param_info.shape[0]):
        param_info.iloc[i].to_csv('RANCH_cluster/MIT_tools/param_dir/param_info_' + str(i) + '.csv', index=False)


if __name__ == '__main__':
    print('entered main script')
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    args = parser.parse_args()
    populate_dir(args)