
from .. import run_model
import pandas as pd
import argparse

# This is a place holder to test the run_trial
def run_Stanford_model(args): 
    # read in the two files: 
    param_info = pd.read_csv(args.param_info_path)
    trial_info = pd.read_csv(args.trial_info_path)

    # testing: 
    trial_info = trial_info.tail(1)

    # loop through trial_info 
    for index, row in trial_info.iterrows():
        run_model.run_trial(param_info = param_info.iloc[0], trial_info = row)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    parser.add_argument("trial_info_path", type=str, help="Path to trial_info csv")
    args = parser.parse_args()    
    run_Stanford_model(args)
