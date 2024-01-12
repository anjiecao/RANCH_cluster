#!/bin/bash -l
#SBATCH --mail-type=END
#SBATCH -n 1 
#SBATCH --mem=4GB
#SBATCH --constraint=30GB
#SBATCH --gres=gpu:1
#SBATCH --time=10:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

project_path=$1
params=("${@:2}")
trial_info="RANCH_cluster/sim_info/trial_info/trial_info_graded_dishab.csv"
current_param_values=${params[${SLURM_ARRAY_TASK_ID}]}

cmd="python -m RANCH_cluster.MIT_tools.run_MIT_cluster_model $current_param_values $trial_info"

echo $cmd 

$cmd