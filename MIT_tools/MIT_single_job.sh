#!/bin/bash -l
#SBATCH --mail-type=END
#SBATCH -n 1 
#SBATCH --mem=2GB
#SBATCH --constraint=20GB
#SBATCH --gres=gpu:1
#SBATCH --time=48:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

project_path=$1
trial_info=("${@:2}")
embedding_info=("${@:3}")
params=("${@:4}")

echo $trial_info
echo $embedding_info
echo $params

current_param_values=${params[${SLURM_ARRAY_TASK_ID}]}

cmd="python -m RANCH_cluster.MIT_tools.run_MIT_cluster_model $current_param_values $trial_info $embedding_info"

echo $cmd 

$cmd