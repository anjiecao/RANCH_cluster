import argparse
from .. import run_model
import pandas as pd

def run_MIT_model(args):

    params = pd.read_csv(args.param_info_path)
    trials = pd.read_csv(args.trial_info_path)

    run_model.run_trial(params, trials)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    parser.add_argument("trial_info", type=str, help="Path to trial_info csv")
    args = parser.parse_args()
    run_MIT_model(args)