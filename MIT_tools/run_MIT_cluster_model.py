from .. import run_model
import pandas as pd
import argparse
import ipdb
import os

def run_MIT_model(args):

    param_names = ['param_id', 'linking_hypothesis', 'mu_prior',
       'hypothetical_obs_grid_n', 'max_observation', 'batch_n', 'jitter_n',
       'quad_a', 'quad_b', 'quad_c', 'V_prior', 'alpha_prior', 'beta_prior',
       'epsilon', 'mu_epsilon', 'sd_epsilon', 'world_EIGs',
       'forced_exposure_max']
        
    params = pd.read_csv(args.param_info_path)

    # make params from list of values to pandas series with param_names as index
    params = pd.Series(params.values[0], index = param_names)
    
    # read trial info
    trials = pd.read_csv(args.trial_info_path)
    
    trials = trials.groupby('trial_id').sample(n=20, replace=True)

    # pass through embeddings csv path
    embeddings = args.embedding_info_path
    
    for _, row in trials.iterrows():

        # run model
        run_model.run_trial(param_info = params, trial_info = row, embeddings = embeddings)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    parser.add_argument("trial_info_path", type=str, help="Path to trial_info csv")
    parser.add_argument("embedding_info_path", type=str, help="Path to embeddings csv")
    args = parser.parse_args()    
    run_MIT_model(args)