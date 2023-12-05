#!/bin/bash -l

project_path="/om2/scratch/tmp/galraz/looking_time_models/04_pyGRANCH_multi_cluster/MIT_cluster_tool/"
param_dir="$project_path/param_job_arr/params/param_vals"

# code that takes eig.csv and creates different files for each row 

param_vals=($(find $param_dir/ -type f))

len=$(expr ${#param_vals[@]} - 1) 

cmd="sbatch --array=0-$len $project_path/MIT_single_job.sh $project_path ${param_vals[@]}" "param_dir/1.csv", "param_dir/2.csv"

$cmd