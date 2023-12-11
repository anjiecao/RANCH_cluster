#!/bin/bash -l

project_path="/om2/scratch/tmp/galraz/RANCH/RANCH_cluster"

param_info=$project_path/sim_info/param_info/eig.csv
param_dir=$project_path/MIT_tools/param_dir

# code that takes eig.csv and creates different files for each row
cmd="python $project_path/MIT_tools/populate_param_dir.py $param_info"

$cmd

param_vals=($(find $param_dir/ -type f))

len=$(expr ${#param_vals[@]} - 1) 

cmd="sbatch --array=0-$len $project_path/MIT_tools/MIT_single_job.sh $project_path ${param_vals[@]}" 

$cmd

