import gc
import torch 
import datetime
from datetime import datetime
import pickle

from .utils import get_jitter_grid, get_embedding, get_sequence

# better way to do this? 
from ..RANCH_model.granch_utils import init_stimuli_tensor, init_params_tensor, init_model_tensor
from ..RANCH_model.granch_utils import main_sim_tensor, proxy_sim, lesioned_sim


def run_trial(param_info, trial_info): 
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    param_info  = param_info.to_dict()
    trial_info = trial_info.to_dict()
    model_type = param_info["linking_hypothesis"]

    # ------ Data structure prepping: ------ #
    # 1. Genereate all the grids used 
    all_jitter_grid = get_jitter_grid.generate_jitter_grid(param_info=param_info)
    
    # 2. Convert Stimuli_info into actual embedding 
    fam, test = get_embedding.string_to_embedding(trial_info=trial_info)
    
    # 3. Convert trial information into sequence
    sequence_scheme = get_sequence.param_to_scheme(trial_info=trial_info)
    # ------ Set up simulation raw material ------ #
    # 4. Set up stimuli
    s = init_stimuli_tensor.granch_stimuli(trial_info["feature_n"], sequence_scheme)
    s.add_stimuli_sequence(fam, test)

    # 5. Set up the parameter

    # ------ Run simulation for one sequence ------ #
    # this is to loop through all the jitter grid 

    for b_i in range(0, param_info["batch_n"]): 
        res_df = pd.DataFrame()
        for i in range(0,param_info["jitter_n"]): 
            tensor_model =  init_model_tensor.granch_model(param_info["max_observation"], s)
            index = b_i * param_info["jitter_n"] + i

            # Here we are setting up the parameters 
            params = init_params_tensor.granch_params(
                grid_mu =  all_jitter_grid["grid_mus"][index].to(device),
                grid_sigma = all_jitter_grid["grid_sigmas"][index].to(device),
                grid_y = all_jitter_grid["grid_ys"][index].to(device),
                grid_epsilon = all_jitter_grid["grid_epsilons"][index].to(device),
                hypothetical_obs_grid_n = param_info["hypothetical_obs_grid_n"], 
                mu_prior = param_info["mu_prior"],
                V_prior = param_info["V_prior"], 
                alpha_prior = param_info["alpha_prior"], 
                beta_prior = param_info["beta_prior"],
                epsilon  = param_info["epsilon"], 
                mu_epsilon = param_info["mu_epsilon"], 
                sd_epsilon = param_info["sd_epsilon"], 
                world_EIGs = param_info["world_EIGs"],

                max_observation = param_info["max_observation"],
                forced_exposure_max = param_info["forced_exposure_max"], 
                linking_hypothesis = param_info["linking_hypothesis"])
            
            params.add_meshed_grid()
            params.add_lp_mu_sigma()
            params.add_y_given_mu_sigma()
            params.add_lp_epsilon()
            params.add_priors()
            


            if model_type == "EIG":
                model = main_sim_tensor.granch_main_simulation(params, tensor_model, s)
            elif model_type == "KL":
                model = proxy_sim.granch_proxy_sim(params, tensor_model, s)
            elif model_type == "surprisal": 
                model = proxy_sim.granch_proxy_sim(params, tensor_model, s)
            elif model_type == "no_learning": 
                model = lesioned_sim.granch_no_learning_simulation(params, tensor_model, s)
            elif model_type == "no_noise": 
                model = lesioned_sim.granch_no_noise_simulation(params, tensor_model, s) 

            # output 
            res = model.output
            res["param_id"] = param_info["param_id"]
            res["trial_id"] = trial_info["trial_id"]
            # uncomment below to store EIG information
            #res = model.behavior
        
            res_df = pd.concat([res_df, res])

        
        curr_time = datetime.now()
        timestr = curr_time.strftime('%m-%d-%H:%M:%S.%f')[:-3] 
        
        batch_name = "cache_results/{t}.pickle".format(t = timestr)
        with open(batch_name, 'wb') as f:
            pickle.dump(res_df, f)
        del res_df
        gc.collect()


# This is a place holder to test the run_trial
def run_sim(param_info_path, trial_info_path): 
    # read in the two files: 
    param_info = pd.read_csv(param_info_path)
    trial_info = pd.read_csv(trial_info_path)

    # testing: 
    trial_info = trial_info.tail(1)

    # loop through trial_info 
    for index, row in trial_info.iterrows():
        run_trial(param_info = param_info.iloc[0], trial_info = row)


run_sim(param_info_path="sim_info/param_info/eig.csv", 
        trial_info_path="sim_info/trial_info/trial_info.csv")