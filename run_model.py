import pandas as pd
# This is the driver file for interacting with the model 
# each run would run the simulation specified in 1 row in param_info and 1 row in trial_info

def run_trial(param_info, trial_info): 
    param_info  = param_info.to_dict()
    trial_info = trial_info.to_dict()

    # genereate batch info (w/ all the jitters)

    # convert stimuli_info into actual embedding 




# This is a place holder to test the run_trial
def run_sim(param_info_path, trial_info_path): 
    # read in the two files: 
    param_info = pd.read_csv(param_info_path)
    trial_info = pd.read_csv(trial_info_path)

    # testing: 
    trial_info = trial_info.head(1)

    # loop through trial_info 
    for index, row in trial_info.iterrows():
        run_trial(param_info = param_info.iloc[0], trial_info = row)


run_sim(param_info_path="sim_info/param_info/eig.csv", 
        trial_info_path="sim_info/trial_info/fake_trial_info.csv")