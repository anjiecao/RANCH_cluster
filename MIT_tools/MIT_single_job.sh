#!/bin/bash -l
#SBATCH --mail-type=END
#SBATCH -n 1 
#SBATCH --mem=8GB
#SBATCH --constraint=40GB
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

params=("${@:2}")
current_param_values=${params[${SLURM_ARRAY_TASK_ID}]}
trial_info="RANCH_cluster/sim_info/param_info/trial_info.csv"

cmd="python -m 04_pyGRANCH_multi_cluster.MIT_cluster_tool.cluster_granch_MIT_param_array $current_param_values $param_names" 

echo $cmd 

$cmd